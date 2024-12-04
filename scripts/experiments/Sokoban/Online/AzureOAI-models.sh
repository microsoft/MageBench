

#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="GPT-4o-Online"
# OUT=""


#====azure endpoint====
export AZOAI_ENDPOINT="https://xxxxxx.openai.azure.com/"

#====model name in the subscription====
MODEL_NAME="gpt4o"


python main.py --API-type AzureOpenAI --model ${MODEL_NAME} --flow-type Online --env Sokoban \
        --output-dir ./output/Sokoban_${SUBSET}/${OUT} \
        --task-path resources/Sokoban_${SUBSET}.json \
        --resolution 640 --temperature 0.1 --n_workers 4 --max_image 1 --max_memory 5 --max_loop 50 --repeat 3 --max_tokens 300
