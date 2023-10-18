from django.http import JsonResponse
import json

     
def api_home(request,*args,**kwargs):
    #request --> HTTP request 
    print(request.GET) # url query params
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # String of JSON data --> Python dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers 
    data['params'] = dict(request.GET)
    data['headers'] =dict(request.headers)
    data['content_type'] = request.content_type
    return  JsonResponse(data)