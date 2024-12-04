

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


python main.py --API-type AzureOpenAI --model ${MODEL_NAME} --flow-type Online --env Football \
        --output-dir ./output/Football_${SUBSET}/${OUT} \
        --task-path resources/Football_${SUBSET}.json \
        --resolution 1280 --temperature 0.1 --n_workers 4 --max_image 1 --repeat 10 --max_tokens 1000 --max_memory 5 --max_loop 400
        

