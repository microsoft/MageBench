
import time

import requests


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


    ag = deepcopy(args)
    port = ag.pop('port')

    ag["message"] = message

    for retry in range(3):
        response = requests.post(f"http://127.0.0.1:{port}/generate/", json=deepcopy(ag))  
        task_id = response.json().get("task_id")  

        result = None
        max_retry = 600
        i_retry = 0
        while True:  
            result_response = requests.get(f"http://127.0.0.1:{port}/result/{task_id}")  
            result_data = result_response.json()  
            if result_data["status"] == "completed":  
                result = result_data["result"]
                if result.startswith("ERROR: "):
                    raise RuntimeError(result)
                return post_process_callback(result)
            else:  
                time.sleep(2)
                i_retry += 1
                if i_retry > max_retry:
                    raise RuntimeError("Something must wrong to wait so long")
        
    raise RuntimeError("Max retry exceed! Please chack your prompt or capture this error.")