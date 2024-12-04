

#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="GPT-4o-Global"
# OUT=""


#====azure endpoint====
export AZOAI_ENDPOINT="https://xxxxxx.openai.azure.com/"

#====model name in the subscription====
MODEL_NAME="gpt4o"


python main.py --API-type AzureOpenAI --model ${MODEL_NAME} --flow-type Global --env Sokoban \
        --output-dir ./output/Sokoban_${SUBSET}/${OUT} \
        --task-path resources/Sokoban_${SUBSET}.json \
        --resolution 640 --temperature 0.1 --n_workers 4 --max_image 1 --repeat 3 --max_tokens 1000
        
