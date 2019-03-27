import requests
import json
import pprint
url = "http://weather.livedoor.com/forecast/webservice/json/v1?city={}"
city_id = 130010
json_url = url.format(city_id)
r = requests.get(json_url)
json = r.json()
pprint.pprint(json)
