

#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="Phi-3-V-Global"
# OUT=""


#====Port you set====
PORT="9000"
# For multi-gpus or multi-ports
# PORT="9000 9001 9002 9003"


#====system message====
# for models in 
# [meta-llama/Llama-3.2-90B-Vision-Instruct, Claude, Gemini], add --model_no_system



python main.py --API-type HuggingFace --flow-type Global --env Sokoban \
        --output-dir ./output/Sokoban_${SUBSET}/${OUT} \
        --task-path resources/Sokoban_${SUBSET}.json \
        --resolution 640 --temperature 0.1 --n_workers 4 --max_image 1 --repeat 3 --max_tokens 1000 \
        --port ${PORT}
