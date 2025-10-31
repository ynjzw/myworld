from django.shortcuts import render
from rest_framework import viewsets
from nodes import models
from nodes.serializer import NodesSerializer,LinksSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def test(request):
    data = 1 + 1
    return Response({'message':data})

# Create your views here.
class NodesViewSet(viewsets.ModelViewSet):
    queryset=models.Nodes.objects.all()
    serializer_class=NodesSerializer


class LinksViewSet(viewsets.ModelViewSet):
    queryset=models.Links.objects.all()
    serializer_class=LinksSerializer
    