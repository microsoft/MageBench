

#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="Phi-3-V-Online-Natural"
# OUT=""


#====Port you set====
PORT="9000"
# For multi-gpus or multi-ports
# PORT="9000 9001 9002 9003"


#====system message====
# for models in 
# [meta-llama/Llama-3.2-90B-Vision-Instruct, Claude, Gemini], add --model_no_system


#====output dir for global setting====
INIT_OUT="Phi-3-V-Global"


#====WebUI online method prompt type
ONLINE_PROMPT="Natural"



python main_WebUI_online.py --API-type HuggingFace --webui_online_type ${ONLINE_PROMPT} \
        --output-dir ./output/Sokoban_${SUBSET}/${OUT} \
        --init-dir ./output/WebUI_${SUBSET}/${INIT_OUT} \
        --task-path resources/Sokoban_${SUBSET}.json \
        --resolution 1920 --temperature 0.1 --n_workers 4 --max_image 10 --repeat 3 --max_tokens 4000 \
        --port ${PORT}
