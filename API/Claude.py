import anthropic, os
from copy import deepcopy
import time
# Create an instance of the Anthropics API client


def process(msg):
    new_msg = []
    sys = ""
    for ms in msg:
        if ms["role"] == "system":
            sys = ms["content"] if isinstance(ms["content"], str) else ms["content"][0]["text"]
            continue
        msn = deepcopy(ms)
        if isinstance(ms["content"], str):
            new_msg.append(msn)
            continue
        for ict in range(len(msn["content"])):
            if msn["content"][ict]["type"] == "image_url":
                msn["content"][ict] = {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": msn["content"][ict]["image_url"]["url"].replace("data:image/jpeg;base64,", "")
                    }
                }
        new_msg.append(msn)
    
    return sys, new_msg
        

def generate(
        message,
        args = {
            "model": "gpt4o",
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 4000
        },
        post_process_callback = lambda x: x
        ):
    
    client = anthropic.Anthropic(api_key= os.getenv("CLAUDE_KEY"))  

    sys, messages = process(message)
    
    if "port" in args:
        args.pop("port")
    if "frequency_penalty" in args:
        args.pop("frequency_penalty")
    
    for retry in range(3):
        try:
            response = client.messages.create(
                            messages=messages,
                            system = sys,
                            **args
                        )
            res = response.content[0].text
            return post_process_callback(res)
            
        except Exception as e:
            if "rate_limit_error" in str(e):
                time.sleep(10)
            print(e)

    raise RuntimeError("Max retry exceed! Please chack your prompt or capture this error.")
