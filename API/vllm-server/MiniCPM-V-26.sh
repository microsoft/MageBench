
echo "Please look at the comments of this file, select your case and comment this line"

# minicpm
# vllm serve openbmb/MiniCPM-V-2_6 --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10  --max_num_seqs 8 --port 9000

# using multiple gpus to deploy multiple endpoints, e.g., 4
# CUDA_VISIBLE_DEVICES=0 vllm serve openbmb/MiniCPM-V-2_6 --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10  --max_num_seqs 8 --port 9000 &
# CUDA_VISIBLE_DEVICES=1 vllm serve openbmb/MiniCPM-V-2_6 --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10  --max_num_seqs 8 --port 9001 &
# CUDA_VISIBLE_DEVICES=2 vllm serve openbmb/MiniCPM-V-2_6 --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10  --max_num_seqs 8 --port 9002 &
# CUDA_VISIBLE_DEVICES=3 vllm serve openbmb/MiniCPM-V-2_6 --max-model-len 32000 \
#     --trust-remote-code --limit-mm-per-prompt image=10  --max_num_seqs 8 --port 9003