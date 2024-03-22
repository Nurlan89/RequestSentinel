from django.urls import path
from .views import gateway

urlpatterns = [
    path("gateway/", gateway, name="my_url"),
]
