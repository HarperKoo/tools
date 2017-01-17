import requests
import json

url = "http://10.213.96.210/getWorker?campid=39&date=2016-11-11"
url2 = "http://10.213.96.210/getRoute?worker=9844&date=2016-11-11"


def readJsonUrl(url):
	req = requests.get(url)
	response=req.content.decode('utf-8')
	json_res = json.loads(response)
	return json_res


# a list
workers = readJsonUrl(url)
# a dict
route = readJsonUrl(url2)

route1 = route.get("route1")