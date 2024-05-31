from django.http import JsonResponse,HttpResponse
import json 
from products.models import Product
from django.forms.models import model_to_dict

def api_home(request, *args, **kwargs):
    # request body
    # body = request.body # byte string of json response
    # model_data = Product.object.all().order_by("?").first()
    # params = dict(request.GET)
    # print(params)
    # print(request.headers)
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # return JsonResponse(data)
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
       data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
    #    data = dict(data)
    #    json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type":"application/json"})