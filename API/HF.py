
import base64

import requests
from openai import OpenAI

def encode_image_base64_from_url(image_url: str) -> str:
    """Encode an image retrieved from a remote url to base64 format."""

    with requests.get(image_url) as response:
        response.raise_for_status()
        result = base64.b64encode(response.content).decode('utf-8')

    return result

def merge_role(message):
    msg_new = deepcopy(message)
    for i in range(len(message)-1, 0, -1):
        if message[i]["role"] == message[i-1]["role"]:
            
            msg_new[i-1]["content"] = msg_new[i-1]["content"] + msg_new[i]["content"]
            msg_new.pop(i)
    return msg_new




from copy import deepcopy

def generate(
        message,
        args = {
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 4000,
            "port": "8000"
        },
        post_process_callback = lambda x: x
        ):
    # Modify OpenAI's API key and API base to use vLLM's API server.
    ag = deepcopy(args)
    port = ag.pop('port')
    openai_api_key = "EMPTY"
    openai_api_base = f"http://localhost:{port}/v1"

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    models = client.models.list()
    model = models.data[0].id
    
    ag["model"] = model
    
    for retry in range(3):
        try:
            response = client.chat.completions.create(
                            messages=merge_role(message),
                            **ag
                        )
            res = response.choices[0].message.content
            return post_process_callback(res)
            
        except Exception as e:
            if 'is too long to fit into the model' in str(e):
                raise RuntimeError("Model input length not enough for this task, you can change a resolution, memory, max-image to resume this.")
            else:
                print(e)
    raise RuntimeError("Max retry exceed! Please chack your prompt or capture this error.")

import json
if __name__ == "__main__":
    ct = json.load(open("/data/home/t2vg-a100-G4-35/zms/LMMAgentBench/resources/WebUI/3D-Nav/tasks_content.json"))
    res = generate(
        [{"role": "system", "content": "Generate the .html, .js, .css file codes according to the information in the description. Generate in code block like ```html\nxxxx```"},
         {"role": "user", "content": ct},]
    )
    res = res.strip()
    for i in range(1000, 1, -1):
        res = res.replace("\n"*i, "\n")
    print(res)