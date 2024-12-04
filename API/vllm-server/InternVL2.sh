
echo "Please look at the comments of this file, select your case and comment this line"



# InternVL2-1b, We found there is a bug if do not add --tensor-parallel-size 2, you can try
# vllm serve OpenGVLab/InternVL2-1B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 --tensor-parallel-size 2

# InternVL2-2b
# vllm serve OpenGVLab/InternVL2-2B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000

# InternVL2-4b
# vllm serve OpenGVLab/InternVL2-4B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000

# InternVL2-8b
# vllm serve OpenGVLab/InternVL2-8B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000

# InternVL2-26b
# vllm serve OpenGVLab/InternVL2-26B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 --tensor-parallel-size 2

# InternVL2-40b
# vllm serve OpenGVLab/InternVL2-40B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 --tensor-parallel-size 2

# using multiple gpus to deploy multiple endpoints, e.g., 4
# CUDA_VISIBLE_DEVICES=0 vllm serve OpenGVLab/InternVL2-8B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 &
# CUDA_VISIBLE_DEVICES=1 vllm serve OpenGVLab/InternVL2-8B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9001 &
# CUDA_VISIBLE_DEVICES=2 vllm serve OpenGVLab/InternVL2-8B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9002 &
# CUDA_VISIBLE_DEVICES=3 vllm serve OpenGVLab/InternVL2-8B --max-model-len 8192 \
#     --trust-remote-code --limit-mm-per-prompt image=10 --port 9003