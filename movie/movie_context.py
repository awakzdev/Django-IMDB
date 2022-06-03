from .models import Movie


def slider_movies(request):
    movie = Movie.objects.last()

    return {'slider_movie': movie}
