from django.http import JsonResponse,HttpResponse
import json 
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
   
   #  instance = Product.objects.all().order_by("?").last()
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      data = serializer.save()
      print(data)
      return Response(serializer.data)
    else:
       return Response({"error":"some fields are reuired"})
  
    
    
    
# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#     # request body
#     # body = request.body # byte string of json response
#     # model_data = Product.object.all().order_by("?").first()
#     # params = dict(request.GET)
#     # print(params)
#     # print(request.headers)
#     # data = {}
#     # try:
#     #     data = json.loads(body)
#     # except:
#     #     pass
#     # print(data)
#     # return JsonResponse(data)
    
#    #  if request.method != "POST":
#       #  return Response({"message":"Status not found!"},status=400)
#     instance = Product.objects.all().order_by("?").last()
#     data = {}
#     if instance:
#        data = model_to_dict(instance, fields=['id', 'title', 'price',"sale_price","my_discount"])
#     return Response(ProductSerializer(instance).data)
#     #    data = dict(data)
#     #    json_data_str = json.dumps(data)
#     # return HttpResponse(json_data_str, headers={"content-type":"application/json"})