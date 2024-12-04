import os
import requests
import base64, json
from azure.identity import AzureCliCredential, get_bearer_token_provider
from openai import AzureOpenAI
import platform

token_provider = get_bearer_token_provider(
    AzureCliCredential(), "https://cognitiveservices.azure.com/.default"
)



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
    
    end_point = os.getenv("AZOAI_ENDPOINT", "https://t2vgoaigpt4o3.openai.azure.com/")

    client = AzureOpenAI(
        api_version="2024-02-15-preview",
        azure_endpoint=end_point,
        azure_ad_token_provider=token_provider
    )
    
    if "port" in args:
        args.pop("port")
    
    for retry in range(3):
        try:
            response = client.chat.completions.create(
                            messages=message,
                            **args
                        )
            res = response.choices[0].message.content
            return post_process_callback(res)
            
        except Exception as e:
            print(e)

    raise RuntimeError("Max retry exceed! Please chack your prompt or capture this error.")


if __name__ == "__main__":
    res = generate(
        [{"role": "system", "content": ""},
         {"role": "user", "content": "hello"},]
    )
    print(res)