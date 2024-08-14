import requests

if __name__=='__main__':
    url = 'https://www.google.com.mx/' #api
    response = requests.get(url)
    print (response)
    
    if response.status_code == 200:
        content = response.content
        #print content in file google.html
        file = open('google.html', 'wb')
        file.write(content)
        file.close()
        