import hmac
import hashlib
import json
import requests

api_key = 'V37UcPDfsVDiaYgs'
secret_key = 'yOjBov7vc-0op26qkHmaLOL4abzb34oK'.encode('utf-8')
query = '/events?filter=that&key=' + api_key
signature = hmac.new(secret_key, query.encode('utf-8'), hashlib.sha1).hexdigest()
url = 'https://api.edinburghfestivalcity.com' + query + '&signature=' + signature

r = requests.get(url)
d = json.loads(r.text)
print(d)
