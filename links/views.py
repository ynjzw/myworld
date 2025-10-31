from django.shortcuts import render
from rest_framework import viewsets
from links.models import Links
# Create your views here.
class LinksViewSet(viewsets.ModelViewSet):
    queryset=Links.objects.all()
    # return render(viewsets.ModelViewSet,'',{'links':queryset})
