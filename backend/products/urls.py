from django.urls import path 

from . import views
from .serializers import ProductSerializer

urlpatterns = [
    # path('', views.product_create_view),
    path('', views.product_list_view),
    path('<int:pk>/', views.product_detail_view),
    
]
