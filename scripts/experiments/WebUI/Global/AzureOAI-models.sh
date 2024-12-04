

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


python main.py --API-type AzureOpenAI --model ${MODEL_NAME} --flow-type Global --env WebUI \
        --output-dir ./output/WebUI_${SUBSET}/${OUT} \
        --task-path resources/WebUI_${SUBSET}.json \
        --resolution 1920 --temperature 0.1 --n_workers 4 --max_image 10 --repeat 3 --max_tokens 4000
        