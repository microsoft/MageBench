

echo "Please look at the comments of this file, select your case and comment this line"

# for 1 GPU testing

# lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9000 --session-len 16000


# using multiple gpus to deploy multiple endpoints, e.g., 4

# CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9000 --session-len 16000 & 
# CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9001 --session-len 16000 &
# CUDA_VISIBLE_DEVICES=2 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9002 --session-len 16000 &
# CUDA_VISIBLE_DEVICES=3 lmdeploy serve api_server deepseek-ai/deepseek-vl-7b-chat --server-port 9003 --session-len 16000 
