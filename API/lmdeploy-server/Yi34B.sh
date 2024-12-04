

echo "Please look at the comments of this file, un-comment your case and comment this line"

# Yi-VL-6B model
# lmdeploy serve api_server 01-ai/Yi-VL-6B --server-port 9000 --session-len 4000

# Yi-VL-34B model
# lmdeploy serve api_server 01-ai/Yi-VL-34B --server-port 9000 --session-len 4000

# if you need (if your GPU mem <= 80G) tensor parallelism
# lmdeploy serve api_server 01-ai/Yi-VL-34B --server-port 9000 --session-len 4000 --tp 2

# using multiple gpus to deploy multiple endpoints for 34B, e.g., 4
# CUDA_VISIBLE_DEVICES=0,1 lmdeploy serve api_server 01-ai/Yi-VL-34B --server-port 9000 --session-len 4000 --tp 2 &
# CUDA_VISIBLE_DEVICES=2,3 lmdeploy serve api_server 01-ai/Yi-VL-34B --server-port 9001 --session-len 4000 --tp 2

# using multiple gpus to deploy multiple endpoints for 6B, e.g., 4
# CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server 01-ai/Yi-VL-6B --server-port 9000 --session-len 4000 &
# CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server 01-ai/Yi-VL-6B --server-port 9001 --session-len 4000 &
# CUDA_VISIBLE_DEVICES=2 lmdeploy serve api_server 01-ai/Yi-VL-6B --server-port 9002 --session-len 4000 &
# CUDA_VISIBLE_DEVICES=3 lmdeploy serve api_server 01-ai/Yi-VL-6B --server-port 9003 --session-len 4000