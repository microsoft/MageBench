import requests  
import time, base64
from PIL import Image
# 发送生成文本的请求  
url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg"
image = Image.open(requests.get(url, stream=True).raw)

image.save("./tmpp.png")
encoded_image = base64.b64encode(open("./tmpp.png", 'rb').read()).decode('ascii')

messages = [
    {"role": "user", "content": [
        {"type": "image_url", "image_url": {
            "url": f"data:image/jpeg;base64,{encoded_image}"
        }},
        {"type": "text", "text": "If I had to write a haiku for this one, it would be: "}
    ]}
]
response = requests.post("http://127.0.0.1:8080/generate/", json={"message": messages})  
task_id = response.json().get("task_id")  
print(f"Task ID: {task_id}")  
  
# 轮询任务状态  
while True:  
    result_response = requests.get(f"http://127.0.0.1:8080/result/{task_id}")  
    result_data = result_response.json()  
    if result_data["status"] == "completed":  
        print("Generated Text:", result_data["result"])  
        break  
    else:  
        print("Task is still pending...")  
        time.sleep(2)  