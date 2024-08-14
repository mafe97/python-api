import requests

url = 'https://pokeapi.co/api/v2/pokemon?'  #api
#bucle while
while url:
    
    payload = {}
    headers = {}
#request get in headers and data payload
    response = requests.request('GET', url, headers=headers, data=payload)
#convert data text to json
    data = response.json()
#print results
    results = data['results']
#bucle for results    
    for result in results:
        name = result['name']
        
    #print(pokemon['name'])
    print (name)
#get result in url
    url = result['url']
#check if there is a next page and update url data
    if "next" in data:
        url = data['next']
    else:
        url = None