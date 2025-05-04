from django.http import HttpResponse
from django.template import loader
from .models import Movie_Table
from django.shortcuts import render
from django.db.models import Q


def movie_search_input(request):
    """
    Renders the HTML form for searching movies.
    """
    return render(request, 'search.html')
def search_movies(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Movie_Table.objects.filter(
            Q(title__icontains=query) |
            Q(genre__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'results.html', context)

def movie_detail(request, movie_id):
    try:
        movie = Movie_Table.objects.get(pk=movie_id)
    except Movie_Table.DoesNotExist:
        # You might want to render a 404 page here
        return render(request, 'details.html', {'movie_id': movie_id})

    context = {
        'movie': movie,
    }
    return render(request, 'details.html', context)
