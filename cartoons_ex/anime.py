import requests

url = 'https://api.jikan.moe/v4/top/anime' #api
data = requests.get(url)
if data.status_code==200:
    #get the json data format
    data = data.json()
    #bucle for data
    for i in data['data']:
    #print title
        print(i['title'])
