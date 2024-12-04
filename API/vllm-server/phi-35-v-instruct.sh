

echo "Please look at the comments of this file, select your case and comment this line"


# phi-3.5-v
# vllm serve microsoft/Phi-3.5-vision-instruct --max-model-len 100000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000

# using multiple gpus to deploy multiple endpoints, e.g., 4
# CUDA_VISIBLE_DEVICES=0 vllm serve microsoft/Phi-3.5-vision-instruct --max-model-len 100000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 &
# CUDA_VISIBLE_DEVICES=1 vllm serve microsoft/Phi-3.5-vision-instruct --max-model-len 100000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9001 &
# CUDA_VISIBLE_DEVICES=2 vllm serve microsoft/Phi-3.5-vision-instruct --max-model-len 100000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9002 &
# CUDA_VISIBLE_DEVICES=3 vllm serve microsoft/Phi-3.5-vision-instruct --max-model-len 100000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9003