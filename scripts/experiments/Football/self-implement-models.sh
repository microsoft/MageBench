

#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="LLAMA32v90B-Online"
# OUT=""


#====Port you set====
PORT="9000"
# For multi-gpus or multi-ports
# PORT="9000 9001 9002 9003"



python main.py --API-type Local --flow-type Online --env Football \
        --output-dir ./output/Football_${SUBSET}/${OUT} \
        --task-path resources/Football_${SUBSET}.json \
        --resolution 1280 --temperature 0.1 --n_workers 4 --max_image 1 --repeat 10 --max_tokens 1000 --max_memory 5 --max_loop 400 \
        --port ${PORT} --model_no_system

