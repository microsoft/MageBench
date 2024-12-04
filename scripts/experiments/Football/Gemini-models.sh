


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


python main.py --API-type Gemini --model ${MODEL_NAME} --flow-type Online --env Football \
        --output-dir ./output/Football_${SUBSET}/${OUT} \
        --task-path resources/Football_${SUBSET}.json \
        --resolution 1280 --temperature 0.1 --n_workers 4 --max_image 1 --repeat 10 --max_tokens 1000 --max_memory 5 --max_loop 400 --model_no_system


