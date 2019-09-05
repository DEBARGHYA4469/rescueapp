import requests,unicodedata 

proxies = {} 


SECRET_KEY_IPSTACK = "xxxxxxxxxxxxxxxxxxxxxxxxx" 

req = requests.get('http://ipinfo.io/ip',proxies=proxies)
ipaddr = unicodedata.normalize('NFKD', req.text).encode('ascii','ignore')

url = 'http://api.ipstack.com/'+ipaddr+'?access_key='+SECRET_KEY_IPSTACK+'&format=1'
ip_json = requests.get(url,proxies=proxies)
jsonData = ip_json.json()

latitude = jsonData['latitude']
longitude = jsonData['longitude']

print(latitude,longitude)


