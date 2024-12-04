from fastapi import FastAPI, BackgroundTasks, HTTPException  
from pydantic import BaseModel  
from typing import Dict  
import requests
import torch
from PIL import Image
from transformers import MllamaForConditionalGeneration, AutoProcessor
import base64  
from io import BytesIO  
from PIL import Image 
from copy import deepcopy

app = FastAPI()  
tasks: Dict[str, str] = {}  

# -----------------------------------------------------------------------------------


model_id = "meta-llama/Llama-3.2-90B-Vision-Instruct"

model = MllamaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_id)
async def run_task(task_id: str, message: list, temperature: float = 0.1, top_p: float = 0.95, max_tokens: int = 4000): 
    msg = deepcopy(message) 
    try:  
        # generate
        images = []
        for role in message:
            for ict in range(len(role["content"])):
                if role["content"][ict]["type"] == "image_url":
                    img_b = role["content"][ict]["image_url"]["url"].replace("data:image/jpeg;base64,", "")
                    image_data = base64.b64decode(img_b)  
                    image_file = BytesIO(image_data)  
                    image = Image.open(image_file)
                    images.append(deepcopy(image))
                    role["content"][ict] = {
                        "type": "image"
                    }

        input_text = processor.apply_chat_template(message, add_generation_prompt=True)
        inputs = processor(
            images if len(images)>0 else None,
            input_text,
            add_special_tokens=False,
            return_tensors="pt",
        ).to(model.device)

        output = model.generate(**inputs, max_new_tokens=max_tokens, temperature=temperature, top_p=top_p)
        out = processor.decode(output[0])
        
        outp = out.split("<|start_header_id|>assistant<|end_header_id|>")[-1].replace("<|eot_id|>", "")
        tasks[task_id] = outp # generated text
    except Exception as e:  
        tasks[task_id] = "ERROR: " + str(e)  
  
# --------------------------------------------------------------------------------------
  
class GenerateRequest(BaseModel):  
    message: list  
    temperature: float = 0.1
    top_p: float = 0.95
    max_tokens: int = 4000
  
@app.post("/generate/")  
async def generate_text(request: GenerateRequest, background_tasks: BackgroundTasks = None):  
    task_id = str(len(tasks) + 1)  
    background_tasks.add_task(run_task, task_id, request.message, request.temperature, request.top_p, request.max_tokens)  
    return {"task_id": task_id}  
  

  
@app.get("/result/{task_id}")  
async def get_result(task_id: str):  
    result = tasks.get(task_id)  
    if result:  
        return {"status": "completed", "result": result}  
    else:  
        return {"status": "pending"}  