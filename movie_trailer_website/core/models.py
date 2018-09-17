import re

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.TextField()
    poster_image_url = models.URLField(max_length=300)
    trailer_youtube_url = models.URLField(max_length=300)

    def __str__(self):
        return self.title

    def get_youtube_id(self):
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        return youtube_id_match.group(0) if youtube_id_match else None
