from gettext import translation
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/683dc465-f4c4-4c48-940b-bd91e4772e0b"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')


def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    frenchTextjson = json.dumps(translation)
    res = json.loads(frenchTextjson)
    frenchText=res["translations"]
    reslast = json.loads(json.dumps(frenchText))
    res1=reslast[0]
    frenchTextlast=res1.get("translation")
    return frenchTextlast


def frenchToEnglish(frenchText):
    #write the code here
    translation= language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    englishTextjson = json.dumps(translation)
    res = json.loads(englishTextjson)
    englishText=res["translations"]
    reslast = json.loads(json.dumps(englishText))
    res1=reslast[0]
    englishTextlast=res1.get("translation")
    return englishTextlast

