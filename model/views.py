from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import FileResponse

from .serializers import FileSerializer

import base64, secrets, io, os


class FileUploadView(APIView):
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):      
        image_folder = './images/' 
        imgdata = base64.b64decode(request.data.get('file'))
        filename = request.data.get('filename')

        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        try:
            with open(os.path.join(image_folder, filename), 'wb') as f:
                f.write(imgdata)
            return Response('Ok', status=status.HTTP_201_CREATED)
        except:
            return Response('Fail', status=status.HTTP_400_BAD_REQUEST)


class ModelVersionView(APIView):

    def get(self, request):
        content = {'version': '0.1'}
        return Response(content)


class SendModelView(APIView):
    permission_classes = [AllowAny]

    def get(self, response):

        img = open('./media/mobilenet.tflite', 'rb')
        response = FileResponse(img)
        return response