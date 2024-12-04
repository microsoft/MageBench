

#====pick a subset====
SUBSET="mini"
# SUBSET="all"


#====write a output dir====
OUT="GPT-4o-Online-Natural"
# OUT=""


#====azure endpoint====
export AZOAI_ENDPOINT="https://xxxxxx.openai.azure.com/"


#====model name in the subscription====
MODEL_NAME="gpt4o"


#====output dir for global setting====
INIT_OUT="GPT-4o-Global"


#====WebUI online method prompt type
ONLINE_PROMPT="Natural"


python main_WebUI_online.py --API-type AzureOpenAI --model ${MODEL_NAME} --webui_online_type ${ONLINE_PROMPT} \
        --output-dir ./output/WebUI_${SUBSET}/${OUT} \
        --init-dir ./output/WebUI_${SUBSET}/${INIT_OUT} \
        --task-path resources/WebUI_${SUBSET}.json \
        --resolution 1920 --temperature 0.1 --n_workers 4 --max_image 10 --repeat 3 --max_tokens 4000
