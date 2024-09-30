
import requests
import json
def emotion_detector(text_to_analyse):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={ "raw_document": { "text": text_to_analyse } }
    response=requests.post(url,json=myobj,headers=header)
    if response.status_code ==200:
        formatted=json.loads(response.text)
        a=formatted['emotionPredictions'][0]['emotion']
        dic={
        'anger':a['anger'] ,
        'disgust': a['disgust'],
        'fear': a['fear'],
        'joy': a['joy'],
        'sadness': a['sadness'] ,
        'dominant_emotion': max(a,key=a.get)
        }
        return dic
    else:
        dic={
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return dic
