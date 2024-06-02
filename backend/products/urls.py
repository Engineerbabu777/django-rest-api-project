from django.urls import path 

from . import views
from .serializers import ProductSerializer

urlpatterns = [
    path('<int:pk>/', views.product_detail_view),
]
