from django.shortcuts import render
from .models import News, Movies
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
import requests
from rest_framework.views import APIView
from django.http import HttpResponse
from decouple import config


# class Homepage(ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
    

# class detailpage(RetrieveUpdateDestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     lookup_field = "id"



class generate_movies(APIView):
    def get(self, request):
        url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

        headers = {
        "accept": "application/json",
        "Authorization": config('movie_key')
        }

        response = requests.get(url, headers=headers)

        a = dict(response.json())

        my_count = Movies.objects.count()

        for i in range(my_count, my_count + 10):

        #     title = a["results"][i]["original_title"]
        #     content = a["results"][i]["overview"]
        #     rating = a["results"][i]["popularity"]
        #     Movies.objects.create(title=title, content=content, rating=rating)

        # return HttpResponse("Generated movies successfully")

