from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

from movie import models as movie_models
from theater import models as theater_models
from django.utils.safestring import mark_safe


class MovieForm(forms.ModelForm):
    class Meta:
        model = movie_models.Movie
        fields = (
            "title",
            "short_plot",
            "plot",
            "director",
            "starring",
            "release_date",
            "running_time",
            "genres",
            "rating",
        )


class MovieMediaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["movie"].widget = forms.HiddenInput()

    class Meta:
        model = movie_models.MovieMedia
        fields = ("movie", "media_type", "image", "video_url")


class ShowTimeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["movie"].widget = forms.HiddenInput()

    class Meta:
        model = theater_models.ShowTime
        fields = ("movie", "hall", "screen_day", "screen_times")
