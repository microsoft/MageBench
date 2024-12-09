import argparse
from API import get_generator


"""
--API-type: for vllm and lmdeploy service, pick HuggingFace
--model: the model of the platform, only need this for AZOAI, OAI, Gemini and Claude
--port: the port, only for HuggingFace and Local
"""



def parse_args():
    parser = argparse.ArgumentParser("Mage Bench")
    parser.add_argument("--API-type", choices = ["HuggingFace", "OpenAI", "AzureOpenAI", "Local", "Gemini", "Claude"], required=True) 
    # api configs
    parser.add_argument("--model", default="gpt4o")
    parser.add_argument("--port", nargs='+', default=["8000"])

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    GENRATOR = get_generator(args)
    generator_parameters = {
            "model": args.model,
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 1000,
            "frequency_penalty": 1.0,
            "port": args.port[0]
        }
    message = [
        {
            "role": "user",
            "content": [{
                "type": "text",
                "text": "hello, who are you?"
            }]
        }
    ]
    output = GENRATOR(message, generator_parameters, lambda x: x)
    
    print("Success! model response of `hello, who are you?` is : \n\n", output)

