from datetime import date, timedelta
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from movie.models import Movie


class IndexView(TemplateView):
    template_name = 'frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        all_movies = Movie.objects.all()
        context['movies'] = all_movies
        context['new_in'] = all_movies
        running_shows = []
        today = date.today()
        i = 0
        for show_date in [today + timedelta(x) for x in range(4)]:
            running_shows.append(
                {'show_date': show_date, 'movies': all_movies[i:]})
            i = i + 1

        context['running_shows'] = running_shows
        context['up_comming_movies'] = all_movies
        return context


class SingleMovie(DetailView):
    template_name = 'frontend/single_movie.html'
    model = Movie
    context_object_name = 'movie'
