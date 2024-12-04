
import google.generativeai as genai
import os
from PIL import Image  
import base64  
from io import BytesIO  

def generate(
        message,
        args = {
            "model": "gemini-1.5-pro",
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 4000,
            "port": "8000"
        },
        post_process_callback = lambda x: x
        ):
    genai.configure(api_key= os.getenv("GEMINI_KEY"))

    messages = []
    for role in message:
        role_content = {
            "role": 'user' if role["role"]=='user' else 'model',
            "parts": []
        }
        for ct in role["content"]:
            if ct["type"] == "text":
                role_content["parts"].append(ct["text"])
            else:
                img_b = ct["image_url"]["url"].replace("data:image/jpeg;base64,", "")  
                image_data = base64.b64decode(img_b)  
                image_file = BytesIO(image_data)  
                image = Image.open(image_file)  
                role_content["parts"].append(image)
        messages.append(role_content)
    

    model = genai.GenerativeModel(args["model"],
                                    generation_config=genai.GenerationConfig(
                                        max_output_tokens=args["max_tokens"],
                                        temperature=args["temperature"],
                                        top_p=args["top_p"],
                                        ))
    
    for retry in range(3):
        try:
            chat = model.start_chat(history=messages[:-1])
            response = chat.send_message(messages[-1]["parts"])
            return post_process_callback(response.text)
        except Exception as e:
            print(e)

    raise RuntimeError("Max retry exceed! Please chack your prompt or capture this error.")




