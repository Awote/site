from kek.views import Test,Registr
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
route = DefaultRouter
urlpatterns = [
    url('image',Test),
    url('users/create',Registr.as_view())
]
