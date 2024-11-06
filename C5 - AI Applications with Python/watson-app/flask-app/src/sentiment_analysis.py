import json
import requests

def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    print(response)
    return response
    ##label = formatted_response['documentSentiment']['label']
    ##score = formatted_response['documentSentiment']['score']
    ##return f"label is {label} and score is {score}"
   