from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Rating(models.Model):
    title = models.CharField(max_length=10)
    age_limit = models.SmallIntegerField()

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=200)
    short_plot = models.CharField(max_length=150)
    plot = models.CharField(max_length=500)
    director = models.CharField(max_length=50)
    starring = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)
    running_time = models.IntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='genres')
    rating = models.ForeignKey(Rating, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_genres(self):
        movie_genres = self.genres.all()
        genres = movie_genres[0].title
        for genre in movie_genres[1:]:
            genres = genres + ', ' + genre.title
        return genres

    def get_feature_image(self):
        feature_image = MovieMedia.objects.filter(movie=self).first()
        return feature_image


class MovieMedia(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="movie_images/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    rate = models.PositiveSmallIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    commented_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user')

    def __str__(self):
        return self.comment
