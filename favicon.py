import requests,mmh3,base64
response = requests.get('https://unomi.apache.org/favicon.ico')
favicon = base64.encodebytes(response.content)
hash = mmh3.hash(favicon)
print(hash)
