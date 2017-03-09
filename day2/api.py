import requests
import json
import pprint
def api(url):
	"""
	This function consumes an api for word's countries names and their capital cities 
	"""
	request_data = requests.get(url)
	status_code = request_data.status_code
	data = request_data.json()

	return data	

url = "http://www.geognos.com/api/en/countries/info/all.json"
pprint.pprint(api(url), width = 1)
	