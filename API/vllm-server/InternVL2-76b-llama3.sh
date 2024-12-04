

vllm serve OpenGVLab/InternVL2-Llama3-76B --max-model-len 8192 \
    --trust-remote-code --limit-mm-per-prompt image=10 --port 8007 \
    --tensor-parallel-size 4