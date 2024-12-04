


#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="Gemini-15-pro-Online-Natural"
# OUT=""


#====model name====
MODEL_NAME="gemini-1.5-pro"

#====key====
export GEMINI_KEY="xxxxxxx"


#====output dir for global setting====
INIT_OUT="Gemini-15-pro-Global"


#====WebUI online method prompt type
ONLINE_PROMPT="Natural"



python main_WebUI_online.py --API-type Gemini --model ${MODEL_NAME} --webui_online_type ${ONLINE_PROMPT} \
        --output-dir ./output/Sokoban_${SUBSET}/${OUT} \
        --init-dir ./output/WebUI_${SUBSET}/${INIT_OUT} \
        --task-path resources/Sokoban_${SUBSET}.json \
        --resolution 1920 --temperature 0.1 --n_workers 4 --max_image 10 --repeat 3 --max_tokens 4000 --model_no_system


