

echo "Please look at the comments of this file, select your case and comment this line"


# llava next mistral 7b
# vllm serve llava-hf/llava-v1.6-mistral-7b-hf --max-model-len 4096 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000

# llava next 34b, you need tp=4 if your GPU mem <= 80G
# vllm serve llava-hf/llava-v1.6-34b-hf --max-model-len 4096 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 \
#     --tensor-parallel-size 4

# using multiple gpus to deploy multiple endpoints, e.g., 4
# CUDA_VISIBLE_DEVICES=0 vllm serve llava-hf/llava-v1.6-mistral-7b-hf --max-model-len 4096 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 &
# CUDA_VISIBLE_DEVICES=1 vllm serve llava-hf/llava-v1.6-mistral-7b-hf --max-model-len 4096 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9001 &
# CUDA_VISIBLE_DEVICES=2 vllm serve llava-hf/llava-v1.6-mistral-7b-hf --max-model-len 4096 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9002 &
# CUDA_VISIBLE_DEVICES=3 vllm serve llava-hf/llava-v1.6-mistral-7b-hf --max-model-len 4096 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9003