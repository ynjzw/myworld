from django.shortcuts import render
from rest_framework import viewsets
from heart.models import Heart
import json
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
from heart.serializer import HeartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view()
def ttt(request):
        test=request.data
        
        return Response(test)
# Create your views here.
class HeartViewSet(viewsets.ModelViewSet):
    queryset=Heart.objects.all()
    serializer_class=HeartSerializer

