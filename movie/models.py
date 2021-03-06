from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.apps import apps
from django.urls import reverse


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
    short_plot = models.CharField(max_length=300)
    plot = models.TextField()
    director = models.CharField(max_length=200)
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
        media_type = MediaType.objects.filter(type='Feature').first()
        feature_image = MovieMedia.objects.filter(
            movie=self, media_type=media_type).first()
        return feature_image

    def get_poster_image(self):
        media_type = MediaType.objects.filter(type='Poster').first()
        poster = MovieMedia.objects.filter(
            movie=self, media_type=media_type).first()
        return poster

    def get_general_images(self):
        media_type = MediaType.objects.filter(type='General').first()
        images = MovieMedia.objects.filter(
            movie=self, media_type=media_type)
        return images

    def get_all_images(self):
        media_type = MediaType.objects.filter(type='Video').first()
        images = MovieMedia.objects.filter(
            movie=self).exclude(media_type=media_type)
        return images

    def get_all_videos(self):
        media_type = MediaType.objects.filter(type='Video').first()
        videos = MovieMedia.objects.filter(
            movie=self, media_type=media_type)
        return videos

    def get_show_times(self):
        ShowTime = apps.get_model('theater', 'ShowTime')
        show_times = ShowTime.objects.filter(movie=self)
        return show_times

    def get_comments(self):
        comments = Comment.objects.filter(movie=self)
        return comments

    def get_slug(self):
        return slugify(self.title)


class MediaType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class MovieMedia(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="movie_images/", blank=True, null=True)
    video_url = models.CharField(max_length=100, blank=True, null=True)
    media_type = models.ForeignKey(
        MediaType, null=True, on_delete=models.SET_NULL)
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

    def get_absolute_url(self):
        return reverse("single_movie", kwargs={"pk": self.movie.id})
