import requests
import json
def api(url):
	request_data = requests.get(url)
	status_code = request_data.status_code
	all_data = request_data.json()
	  

	return all_data


url = "http://www.geognos.com/api/en/countries/info/all.json"
print(api(url))
	