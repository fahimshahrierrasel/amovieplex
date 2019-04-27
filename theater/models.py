from django.db import models
from movie.models import Movie


class HallType(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Hall(models.Model):
    name = models.CharField(max_length=100)
    hall_type = models.ForeignKey(
        HallType, null=True, blank=True,
        on_delete=models.SET_NULL)
    desc = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ScreenTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


class ScreenDay(models.Model):
    day = models.CharField(max_length=10)
    is_holiday = models.BooleanField(default=False)

    def __str__(self):
        return self.day


class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    screen_day = models.ForeignKey(
        ScreenDay, null=True, blank=True,
        on_delete=models.SET_NULL)
    screen_times = models.ManyToManyField(
        ScreenTime, related_name='screen_times')

    def __str__(self):
        return f'{self.movie.title}-{self.hall.name}-{self.screen_day.day}'
