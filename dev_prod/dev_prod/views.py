from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .enviroment_status import Enviroment
from .prod_dev import *
import os


class JsonView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        response = {
            "APP_ENV": Enviroment.env,
        }
        return Response(response, status=status.HTTP_200_OK)


class proverkaObnoviView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        if Enviroment.env=='Production' or Enviroment.env=='Development':
            text_response = 'Это сообщение выведется на' + Enviroment.env
        else:
            text_response = 'Переменная окружения не задана'
        response = {
            "Сообщение": text_response,
        }
        return Response(response, status=status.HTTP_200_OK)
