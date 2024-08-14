import requests
import json

"""
#basic requests

url = 'https://rickandmortyapi.com/api/character/2' #api
data = requests.get(url)
j = data.json()

status = j['status']
print (status)

i = 1

while i < 11:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(i) #api
    data = requests.get(url)
    j = data.json()
    name = j['name']
    status = j['status']
    print('The character {} has status: {}'.format(name, status))
    i += 1
"""    
#request to first episode
url = 'https://rickandmortyapi.com/api/episode/1' #api
data = requests.get(url)
j = data.json()
print(j['name'])
characters = j['characters']
list_names = list()
list_names_human = list()
list_names_other = list()

for character in characters:
    req = requests.get(character)
    js = req.json()
    name = js['name']
    if js['species'] == 'Human':
        list_names_human.append(name)
    else:
        list_names_other.append(name)
        
print('Others:', list_names_other)
print('Humans:', list_names_human)