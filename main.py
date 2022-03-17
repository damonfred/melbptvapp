import json
import requests
from generatekey import getUrl


route_type = 0
route_id = 11
stop_id = 1011
request_url = '/v3/routes'
# request_url = f'/v3/departures/{route_type}/stop/{stop_id}/{route_id}'
ptv_response =  getUrl(request_url)
ptv_url = ptv_response[0]


response = requests.get(ptv_url)


ptv_dict = json.loads(response.content)

print(ptv_dict)