from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
import os
from django.core.files import File
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework.views import APIView
from kek.serialization import UserSeria
# Create your views here.
@api_view(['POST'])
def Test(request):

    # print(type(request.FILES['profile']))
    data = request.FILES['profile']  # or self.files['image'] in your form

    path = default_storage.save('tes_video.MOV', ContentFile(data.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    return Response({'GFXHJG':'GHJLK'})



class Registr(APIView):
    def post(self,request):
        print(request.query_params)
        serializer = UserSeria(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Greate user regist':'True'})
