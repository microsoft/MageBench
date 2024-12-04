

echo "Please look at the comments of this file, un-comment your case and comment this line"

# xcomposer2-7b model
# lmdeploy serve api_server internlm/internlm-xcomposer2-vl-7b --server-port 9000 --session-len 4000

# xcomposer2-1.8b model
# lmdeploy serve api_server internlm/internlm-xcomposer2-vl-1_8b --server-port 9000 --session-len 4000

# using multiple gpus to deploy multiple endpoints, e.g., 4
# CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server internlm/internlm-xcomposer2-vl-1_8b --server-port 9000 --session-len 4000 &
# CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server internlm/internlm-xcomposer2-vl-1_8b --server-port 9001 --session-len 4000 &
# CUDA_VISIBLE_DEVICES=2 lmdeploy serve api_server internlm/internlm-xcomposer2-vl-1_8b --server-port 9002 --session-len 4000 &
# CUDA_VISIBLE_DEVICES=3 lmdeploy serve api_server internlm/internlm-xcomposer2-vl-1_8b --server-port 9003 --session-len 4000