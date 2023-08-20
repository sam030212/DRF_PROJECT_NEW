from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myappone.models import Movie

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()

    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)

def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)

    data = {
        'movies':movie.name,
        'description':movie.description,
        'active':movie.active

    }

    return JsonResponse(data)