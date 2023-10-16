import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"Hello Python"}) # HTTP request
                # >> API method 
                # RestAPI's >> Web API

 
print(get_response.json()) # print the raw text response

# HTTP request > HTML >> made for humans 
# RESTAPI HTTP request > JSON (xml) >> made for SW
# JSON >> Java Script Object Notion


# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.31.0", 
#     "X-Amzn-Trace-Id": "Root=1-652db1ec-4ab2f84c12f07fd6186e4f22" >> JSON Response
#   }, 
#   "json": null, 
#   "method": "GET", 
#   "origin": "156.197.160.108", 
#   "url": "https://httpbin.org/anything"
# }



# python dict {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-652db28f-533eed03589ebecc5319506a'}, 'json': None, 'method': 'GET', 'origin': '156.197.160.108', 'url': 'https://httpbin.org/anything'}

print(get_response.status_code)