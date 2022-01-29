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
          "environment": Enviroment.env,
      }
      return Response(response, status=status.HTTP_200_OK)
