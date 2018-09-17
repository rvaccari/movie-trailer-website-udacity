from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from movie_trailer_website.core.models import Movie


class Command(BaseCommand):

    def _create_admin(self):
        email = settings.USER_ADMIN_EMAIL
        username = email.split('@')[0]
        password = settings.USER_ADMIN_PASS
        admin = User.objects.create_superuser(username=username, email=email, password=password)
        admin.save()

    def _init_data(self):
        Movie.objects.bulk_create([
            Movie(title="Toy Story 1",
                  storyline="A story of a boy and his toys that come to life",
                  poster_image_url="https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  trailer_youtube_url="https://www.youtube.com/watch?v=KYz2wyBy3kc"),
            Movie(title="Avatar",
                  storyline="A marine on an alien planet",
                  poster_image_url="https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                  trailer_youtube_url="https://www.youtube.com/watch?v=5PSNL1qE6VY"),
            Movie(title="Matrix",
                  storyline="A dystopian future in which reality as perceived by most humans is actually a simulated reality called the Matrix",
                  poster_image_url="https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                  trailer_youtube_url="https://www.youtube.com/watch?v=m8e-FF8MsqU"),
            Movie(title="Star Wars",
                  storyline="An epic battle a long time ago in another galaxy.",
                  poster_image_url="https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                  trailer_youtube_url="https://www.youtube.com/watch?v=vZ734NWnAHA"),
            Movie(title="Wonder Woman",
                  storyline="Diana Prince arrives to London leaving her home to fight God Zeus",
                  poster_image_url="https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                  trailer_youtube_url="https://www.youtube.com/watch?v=VSB4wGIdDwo"),
        ])

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            self._create_admin()
            self._init_data()
