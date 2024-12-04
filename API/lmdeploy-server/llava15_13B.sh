
echo "Please look at the comments of this file, un-comment your case and comment this line"

# llava 7b models
# lmdeploy serve api_server liuhaotian/llava-v1.5-7b --server-port 9000 --session-len 4096

# llava 13b models
# lmdeploy serve api_server liuhaotian/llava-v1.5-13b --server-port 9000 --session-len 4096

# if you need a tensor parallelism
# lmdeploy serve api_server liuhaotian/llava-v1.5-13b --server-port 9000 --session-len 4096 --tp 2

# using multiple gpus to deploy multiple endpoints, e.g., 4
# CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server liuhaotian/llava-v1.5-7b --server-port 9000 --session-len 4096 & 
# CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server liuhaotian/llava-v1.5-7b --server-port 9001 --session-len 4096 &
# CUDA_VISIBLE_DEVICES=2 lmdeploy serve api_server liuhaotian/llava-v1.5-7b --server-port 9002 --session-len 4096 &
# CUDA_VISIBLE_DEVICES=3 lmdeploy serve api_server liuhaotian/llava-v1.5-7b --server-port 9003 --session-len 4096

