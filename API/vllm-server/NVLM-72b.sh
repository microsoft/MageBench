

vllm serve nvidia/NVLM-D-72B --max-model-len 32000 \
    --trust-remote-code --limit-mm-per-prompt image=10 --port 9000 \
    --tensor-parallel-size 4