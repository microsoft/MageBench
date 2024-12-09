# Setup Service
> The general idea is that we make treat all models as a API service, with [OpenAI's](https://platform.openai.com/docs/api-reference/chat) input format, such that during agent implementation, we could use a unified code to access all models only adjusting few settings. 

## Model/platform You want to implement
- [Azure OpenAI platform (GPT-4o / 4o-mini / 4v)](#Azure-OpenAI-platform)
- [Gemini platform (Gemini-1.5-pro / flash / flash-8B)](#Gemini-platform)
- [Claude platform (Claude-3.5-Sonnet / Haiku / Opus)](#Claude-platform)
- [VLLM service (InternVL2-x, llava-v1.6-mistral-x, MiniCPM-V-2_6, NVLM-D-72B, Phi-3.5-vision-instruct, Qwen2-VL-x)](#VLLM-service)
- [LMDeploy service (deepseek-vl-7b-chat, llava-v1.5-x, internlm-xcomposer2-vl-x, Yi-VL-x)](#LMDeploy-service)
- [OpenAI platform (ongoing...)](#OpenAI-platform)
- [Implement a new model (models not supportted above)](#implement-a-new-model)

## Azure OpenAI platform
Azure OpenAI platform do not use API key, instead, it use `az login` to provide local credit.
To install the azure packages, in the main dir of this repo, run:
```bash
bash ./scripts/install/AzureOpenAI.sh
```
Then finish the `az login`. You will need to `az login` every 12h.

## Gemini platform
To install the Gemini API packages, in the main dir of this repo, run:
```bash
bash ./scripts/install/Gemini.sh
```
please refer to [API document](https://ai.google.dev/gemini-api/docs/downloads?hl=en) if you have any issues. 


## Claude platform
To install the Claude API packages, in the main dir of this repo, run:
```bash
bash ./scripts/install/Claude.sh
```
please refer to [API document](https://docs.anthropic.com/en/docs/initial-setup) if you have any issues. 


## VLLM service

We put vllm in the project requirements so you do not need any extra installations. **(1)** You need to start a model service in backstage. To do this, you should first start a new tmux session (suggested), or screen, or new terminal:
```bash
tmux new -s service
```
**(2)** Then, in the new session, start the docker (the same docker with the environment).
**(3)** Go to `./API/vllm-server` dir to find your target models, read the comments in the `.sh` file carefully, adapt the `.sh` file and **(4)** run your target file. Refer to [here](#vllm--lmdeploy-details) for further details of advanced usage. 

## LMDeploy service

LMDeploy has some requirements conflict with the main environment, so you will need a new docker. **(1)** You need to start a model service in backstage. To do this, you should first start a new tmux session (suggested), or screen, or new terminal:
```bash
tmux new -s service
```
**(2)** Then, in the new session, start a new separate docker, it can be staring with the environment's docker. and run:
```bash
bash ./scripts/install/LMdeploy.sh
```
**(3)** Go to `./API/lmdeploy-server` dir to find your target models, read the comments in the `.sh` file carefully, adapt the `.sh` file and **(4)** run your target file. Refer to [here](#vllm--lmdeploy-details) for further details of advanced usage. 

## OpenAI platform

Ongoing......We use Azure OpenAI platform. There may be a little gap between OAI models and AZOAI models.

## Implement a new model

For models not supported above, we wrote a self-implemented service using uvicorn and fast api. We provide one example (Llama-3.2-90B-Vision-Instruct) in ./API/OurServer dir. You will have to implement the generation code to setup a new model.



## VLLM & LMDeploy details

### About Multi-GPUs accelerating
For large models that need tenser-parallelism, you may use multi-GPUs for one model service. For smaller models, in order to leverage multiple GPUs, we just start multiple services like:
```bash
CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9000 --session-len 16000 & 
CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9001 --session-len 16000 &
CUDA_VISIBLE_DEVICES=2 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9002 --session-len 16000 &
CUDA_VISIBLE_DEVICES=3 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9003 --session-len 16000 
```
Then in the main.py, set:
```bash
--port 9000 9001 9002 9003
```
and let `--n_workers` larger than the number of services. 
For more examples, if you have 4 GPUs and a model with tp=2, then you can start 2 services with the similar method as the above.