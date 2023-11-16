from django.shortcuts import render
from movies.models import Movie
from ratings.models import MovieRating
from django.db.models import Avg, Count, Max
import random

def index(request):
    all_movies = list(Movie.objects.all())
    random_movies = random.sample(all_movies, min(len(all_movies), 6))

    movies_with_ratings = []
    for movie in random_movies:
        ratings = MovieRating.objects.filter(movie=movie)
        if ratings.exists():
            average_rating = ratings.aggregate(Avg('overall_rating'))['overall_rating__avg']
        else:
            average_rating = 'No ratings yet'

        movies_with_ratings.append({
            'movie': movie,
            'title': movie.title,
            'year': movie.year,
            'duration': movie.duration,
            'star_rating': movie.star_rating,
            'average_rating': average_rating,
            'image_url': movie.image_url if movie.image_url else None
        })

    return render(request, 'index.html', {'movies_with_ratings': movies_with_ratings})



def search_results(request):
    query = request.GET.get('query', '')

    if query:
        movies = Movie.objects.filter(title__icontains=query) | Movie.objects.filter(year__icontains=query)
        return render(request, 'search_results.html', {'movies': movies, 'query': query})
    else:
        return redirect('index')