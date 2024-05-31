from django.http import JsonResponse
import json 
from products.models import Product
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
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
    return JsonResponse(data)