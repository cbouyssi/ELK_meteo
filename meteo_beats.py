import os
import requests
import json
import time

f = open('villesmonde.txt', 'r')
ff = open('mapping2.json', 'r')

# req1 = requests.put('http://tc405-112-03:9200/meteogeoloc10', json=json.load(ff))


while True:
    for ville in f:
        try:
            ville = ville.replace("\n", "")
            req = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=464e44d2007c5727857bc4f02d965013".format(ville)
            print(ville)

            res = requests.get(req)
            data = res.text
            data = data.replace("null", "None")
            splitData = data.split("[")
            debut=splitData[0]

            splitData1 = splitData[1].split("]")

            fin=splitData1[1]
            listweather=splitData1[0]
            listweatherSplit=listweather.split(",{\"id\"")
            data = debut + listweatherSplit[0] + fin
            dic = json.loads(data)


            res = requests.post('http://tc405-112-03:9200/meteogeoloc10/_doc', json=dic)

        except ValueError and Exception:
            pass

    time.sleep(1800)        #wait 30min
