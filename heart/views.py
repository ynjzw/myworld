from django.shortcuts import render
from rest_framework import viewsets
from heart.models import Heart
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from heart.serializer import HeartSerializer
# Create your views here.
class HeartViewSet(viewsets.ModelViewSet):
    queryset=Heart.objects.all()
    serializer_class=HeartSerializer

