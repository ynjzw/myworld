from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from nodes import models
from nodes.serializer import NodesSerializer,LinksSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def test(request):
    return Response({'message':'hell'})
