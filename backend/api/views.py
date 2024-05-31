from django.http import JsonResponse
import json 
def api_home(request, *args, **kwargs):
    # request body
    body = request.body # byte string of json response
    params = dict(request.GET)
    print(params)
    print(request.headers)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse(data)