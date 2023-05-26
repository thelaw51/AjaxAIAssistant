import requests
import json
import urllib.request
import playsound
import os
import whisper
import speech_recognition as sr


def CarterSpeakCall():
    response = requests.post(
        "https://api.carterlabs.ai/speak",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"text": "Pee pee poo poo", "key": "2b24f088-93cd-4a82-84a2-296f7d123e6b", "voice_id": "male"}),
    )
    return response.json()


def CarterOpenerCall():
    response = requests.post(
        "https://api.carterlabs.ai/opener",
        headers={"Content-Type": "application/json", "Accept": "*/*"},
        data=json.dumps(
            {"key": "2b24f088-93cd-4a82-84a2-296f7d123e6b", "playerId": "Thelaw51", "personal": True, "speak": True}
        ),
    )
    return response.json()


def CarterChatCall():
    response = requests.post(
        "https://api.carterlabs.ai/chat",
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {
                "text": text,
                "key": "2b24f088-93cd-4a82-84a2-296f7d123e6b",
                "playerId": "Thelaw51",
                "speak": True,
            }
        ),
    )
    return response.json()


def VoiceRecog():
    Recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = Recogniser.listen(source)
        return audio


def SpeechToText(audio):
    try:
        Recogniser = sr.Recognizer()
        text = Recogniser.recognize_whisper(audio, language="english", model="tiny")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")


def AssisstantAudioOutput(jsonResponse):
    responseAudioURL = jsonResponse["output"]["audio"]
    urllib.request.urlretrieve(responseAudioURL, "voice.mp3")
    playsound.playsound("voice.mp3")
    os.remove("voice.mp3")
    if "goodbye" in jsonResponse["output"]["text"] or "Goodbye" in jsonResponse["output"]["text"]:
        os._exit(0)


def UserInput():
    audio = VoiceRecog()
    text = SpeechToText(audio)
    return text


listening = True
while listening == True:
    text = UserInput()
    if "Hey, Ajax" in text:
        Converse = True
        ConverseCount = 0
        while Converse == True:
            ConverseCount += 1
            jsonResponse = CarterChatCall()
            AssisstantAudioOutput(jsonResponse)
