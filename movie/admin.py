from django.contrib import admin
from .models import Genre, Rating, Movie, MovieMedia, Comment, MediaType

admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(MovieMedia)
admin.site.register(MediaType)
admin.site.register(Comment)
