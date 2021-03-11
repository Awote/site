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

def Test(request):

    # print(type(request.FILES['profile']))
    data = request.FILES['profile']  # or self.files['image'] in your form

    path = default_storage.save('tes_video.MOV', ContentFile(data.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    return Response({'Video':'Send'})



class Registr(APIView):
# @api_view(['GET'])
    def post(self,request):

        serializer = UserSeria(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Greate user regist':'True'})
        else:
           return Response({"Error":"CHECK"})
