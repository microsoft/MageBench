

#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="LLAMA32v90B-Global"
# OUT=""


#====Port you set====
PORT="9000"
# For multi-gpus or multi-ports
# PORT="9000 9001 9002 9003"



python main.py --API-type Local --flow-type Global --env WebUI \
        --output-dir ./output/WebUI_${SUBSET}/${OUT} \
        --task-path resources/WebUI_${SUBSET}.json \
        --resolution 1920 --temperature 0.1 --n_workers 4 --max_image 1 --repeat 3 --max_tokens 4000 \
        --port ${PORT} --model_no_system

