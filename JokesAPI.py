# from urllib import request
import requests  #The Standard for request is requests library
import json
import pyttsx3

url = "https://official-joke-api.appspot.com/random_ten"
# r = request.urlopen(url)
# print(r.getcode())

response= requests.get(url) #Request module Functions
print(response.status_code)

jsonData = json.loads(response.text)
print(jsonData)

class Joke:

    def __init__(self,setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup: {self.setup} punchline: {self.punchline}"

#Intializing Array Object
jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup,punchline)
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")

for joke in jokes:
    print(joke)
    pyttsx3.speak("setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("The Punch Line")
    pyttsx3.speak(joke.punchline)