from django.shortcuts import render
from .models import News
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
import requests


class Homepage(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

class detailpage(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"