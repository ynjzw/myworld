from django.shortcuts import render
from rest_framework import viewsets
from nodes import models
from nodes.serializer import NodesSerializer,LinksSerializer,FamilySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from ollama import chat
from ollama import ChatResponse
from django.db.models import F
import pyttsx3
@api_view()
def ttt(request):
        test=request.data
        
        return Response(test)
@api_view()
def test(request):
    engine = pyttsx3.init()
    engine.say("I will speak this text")
    engine.runAndWait()
    return Response({'message':'ok'})
    

@api_view(['POST','GET'])
def test1(request):
    if request.method == 'POST':
        response: ChatResponse = chat(model='deepseek-r1:1.5b', messages=[
            {
                'role': 'user',
                'content': request.data,
            },
        ])
        return Response(response.message.content)

@api_view()
def test2(request):
    data=models.Nodes.objects.filter(name__exact='node1').all()
    return Response(data)


# Create your views here.
class NodesViewSet(viewsets.ModelViewSet):
    queryset=models.Nodes.objects.filter(name__exact='node1').all()
    serializer_class=NodesSerializer


class LinksViewSet(viewsets.ModelViewSet):
    queryset=models.Links.objects.all()    
    serializer_class=LinksSerializer
    

class FamilyViewSet(viewsets.ModelViewSet):
    queryset=models.Family.objects.all()
    
    serializer_class=FamilySerializer
    
    