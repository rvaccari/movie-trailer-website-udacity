from django.shortcuts import render

from movie_trailer_website.core.models import Movie


def index(request):
    template_name = 'core/index.html'
    ctx = {'movies': Movie.objects.all()}
    return render(request, template_name, ctx)
