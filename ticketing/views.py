from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from ticketing.models import Movie, Cinema


def movie_list(request):
    movies = Movie.objects.all()
    count = len(movies)
    context = {
        'movies': movies,
        'movie_count': count
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = Cinema.objects.all()
    context = {
        'cinemas': cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)


def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    """
        Use get() to return an object, or raise a Http404 exception if the object
        does not exist.

        klass may be a Model, Manager, or QuerySet object. All other passed
        arguments and keyword arguments are used in the get() query.

        Like with QuerySet.get(), MultipleObjectsReturned is raised if more than
        one object is found.
    """
    context = {
        'movie': movie
    }
    return render(request, 'ticketing/movie_details.html', context)


def cinema_details(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)
    # return HttpResponse(cinema)