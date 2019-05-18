from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


from movie.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'short_plot', 'plot', 'director', 'starring',
                  'release_date', 'running_time', 'genres', 'rating')
