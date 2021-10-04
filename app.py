from flask import Flask
import requests

app = Flask(__name__)
my_city = "Zelenograd"
api_key = "8486e0f2b96cc24feebf8c51524b9fc6"

def finder():
    res = requests.get(f"http://api.openweathermap.org/data/2.5/find?q={my_city}&type=like&APPID={api_key}")
    data = res.json()
    print("Temperature in Zelenograd: ", str(int(data['list'][0]['main']['temp']) - 273) + " degrees")

@app.route('/')
def hello_world():
    return finder()
