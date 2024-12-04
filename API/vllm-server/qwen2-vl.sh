
echo "Please look at the comments of this file, select your case and comment this line"

# qwen 7B
# vllm serve Qwen/Qwen2-VL-7B-Instruct --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000

# qwen 2B
# vllm serve Qwen/Qwen2-VL-2B-Instruct --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000

# qwen 72B use tp=4 if your GPU mem = 80GB
# vllm serve Qwen/Qwen2-VL-72B-Instruct --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 \
#     --tensor-parallel-size 4

# using multiple gpus to deploy multiple endpoints, e.g., 4
# CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen2-VL-7B-Instruct --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 &
# CUDA_VISIBLE_DEVICES=1 vllm serve Qwen/Qwen2-VL-7B-Instruct --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9001 &
# CUDA_VISIBLE_DEVICES=2 vllm serve Qwen/Qwen2-VL-7B-Instruct --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9002 &
# CUDA_VISIBLE_DEVICES=3 vllm serve Qwen/Qwen2-VL-7B-Instruct --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9003