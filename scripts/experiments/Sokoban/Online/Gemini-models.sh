


#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="Gemini-15-pro-Online"
# OUT=""


#====model name====
MODEL_NAME="gemini-1.5-pro"

#====key====
export GEMINI_KEY="xxxxxxx"


python main.py --API-type Gemini --model ${MODEL_NAME} --flow-type Online --env Sokoban \
        --output-dir ./output/Sokoban_${SUBSET}/${OUT} \
        --task-path resources/Sokoban_${SUBSET}.json \
        --resolution 640 --temperature 0.1 --n_workers 4 --max_image 1 --max_memory 5 --max_loop 50 --repeat 3 --max_tokens 300 --model_no_system


