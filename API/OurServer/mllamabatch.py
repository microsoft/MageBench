from fastapi import FastAPI, BackgroundTasks, HTTPException  
from pydantic import BaseModel  
from typing import List, Dict  
import requests  
import torch  
from PIL import Image  
from transformers import MllamaForConditionalGeneration, AutoProcessor  
import base64  
from io import BytesIO  
from copy import deepcopy  
import asyncio  
  
app = FastAPI()  
  
tasks: Dict[str, str] = {}  
task_queue: List[Dict] = []  
  
# 加载GPT模型  
model_id = "meta-llama/Llama-3.2-90B-Vision-Instruct"  
model = MllamaForConditionalGeneration.from_pretrained(  
    model_id,  
    torch_dtype=torch.bfloat16,  
    device_map="auto",  
)  
processor = AutoProcessor.from_pretrained(model_id)  
  
async def run_task_batch():  
    while True:  
        if len(task_queue) > 0:  
            batch_tasks = task_queue[:10]  # 每次处理10个任务  
            task_queue[:] = task_queue[10:]  # 更新队列  
            await process_batch(batch_tasks)  
        await asyncio.sleep(5)  # 每隔5秒检查一次任务队列  
  
async def process_batch(batch_tasks: List[Dict]):  
    messages = [deepcopy(task['message']) for task in batch_tasks]  
    task_ids = [task['task_id'] for task in batch_tasks]

    temper = batch_tasks[0]["temperature"]
    tp= batch_tasks[0]["top_p"]
    mtks = batch_tasks[0]["max_tokens"]
      
    try:  
        images_list = []  
        inputs_list = []  
  
        for message in messages:  
            images = []  
            for role in message:  
                for ict in range(len(role["content"])):  
                    if role["content"][ict]["type"] == "image_url":  
                        img_b = role["content"][ict]["image_url"]["url"].replace("data:image/jpeg;base64,", "")  
                        image_data = base64.b64decode(img_b)  
                        image_file = BytesIO(image_data)  
                        image = Image.open(image_file)  
                        images.append(deepcopy(image))  
                        role["content"][ict] = {"type": "image"}  
  
            input_text = processor.apply_chat_template(message, add_generation_prompt=True)  
            inputs = processor(  
                images if len(images) > 0 else None,  
                input_text,  
                add_special_tokens=False,  
                return_tensors="pt",  
            ).to(model.device)  
            images_list.append(images)  
            inputs_list.append(inputs)  
  
        # Batch processing  
        batched_inputs = {key: torch.cat([inputs[key] for inputs in inputs_list], dim=0) for key in inputs_list[0]}  
        output = model.generate(**batched_inputs, max_new_tokens=mtks, temperature=temper, top_p=tp)  
          
        for i, task_id in enumerate(task_ids):  
            out = processor.decode(output[i])  
            outp = out.split("<|start_header_id|>assistant<|end_header_id|>")[-1].replace("<|eot_id|>", "").replace("<|finetune_right_pad_id|>", "")
            tasks[task_id] = outp  
  
    except Exception as e:  
        for task_id in task_ids:  
            tasks[task_id] = "ERROR: " + str(e)  
  
class GenerateRequest(BaseModel):  
    message: list  
    temperature: float = 0.1  
    top_p: float = 0.95  
    max_tokens: int = 4000  
  
@app.post("/generate/")  
async def generate_text(request: GenerateRequest, background_tasks: BackgroundTasks = None):  
    task_id = str(len(tasks) + 1)  
    task = {  
        "task_id": task_id,  
        "message": request.message,  
        "temperature": request.temperature,  
        "top_p": request.top_p,  
        "max_tokens": request.max_tokens  
    }  
    task_queue.append(task)  
    return {"task_id": task_id}  
  
@app.get("/result/{task_id}")  
async def get_result(task_id: str):  
    result = tasks.get(task_id)  
    if result:  
        return {"status": "completed", "result": result}  
    else:  
        return {"status": "pending"}  
  
# 启动后台任务处理  
@app.on_event("startup")  
async def startup_event():  
    asyncio.create_task(run_task_batch())  