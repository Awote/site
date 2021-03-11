from kek.views import Test,Registr
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
route = SimpleRouter
urlpatterns = [
    url(r'image',Test),
    url(r'users/create',Registr.as_view())
]
# urlpatterns=route.urls