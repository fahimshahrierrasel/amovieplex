from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from movie import models as movie_models
from theater import models as theater_models
from . import forms
from django.http import HttpResponse
from django.core import serializers


class LoginView(LoginView):
    template_name = "dashboard/auth/login.html"
    redirect_authenticated_user = True
    extra_context = {"page_title": "Admin Login"}

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse("dashboard.index")


class LogoutView(LogoutView):
    next_page = "/admin/dashboard/login"


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Dashboard"}
    template_name = "dashboard/index.html"


class MovieListView(LoginRequiredMixin, ListView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Movies"}
    template_name = "dashboard/movies/movie_list.html"
    model = movie_models.Movie
    context_object_name = "movies"
    ordering = ["-release_date"]


class MovieDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = movie_models.Movie
    template_name = "dashboard/movies/movie_detail.html"
    extra_context = {"page_title": "Movie Detail"}
    form_class = forms.MovieMediaForm

    def get_success_url(self):
        return reverse("dashboard.movie.detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        media_form = self.get_form()
        media_form.fields["movie"].initial = self.object.pk
        context["form"] = media_form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            # Has some bug form resubmission occur in reload on invalid form
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.save()
        return redirect(self.get_success_url())


class MovieCreateView(LoginRequiredMixin, CreateView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "New Movie"}
    model = movie_models.Movie
    form_class = forms.MovieForm
    template_name = "dashboard/movies/movie_form.html"


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Update Movie"}
    model = movie_models.Movie
    form_class = forms.MovieForm
    template_name = "dashboard/movies/movie_form.html"
    success_url = reverse_lazy("dashboard.movie.list")


class MovieMediaView(LoginRequiredMixin, FormMixin, TemplateView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Movie Medias"}
    template_name = "dashboard/movie_medias/index.html"
    form_class = forms.MovieMediaForm

    def get_success_url(self):
        return reverse("dashboard.medias")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_movies = movie_models.Movie.objects.all()
        context["movies"] = all_movies
        media_form = self.get_form()
        media_form.fields["movie"].initial = all_movies[0].id
        context["form"] = media_form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            # Has some bug form resubmission occur in reload on invalid form
            return self.form_invalid(form)

    def form_valid(self, form):
        movie_media = form.save(commit=False)
        movie_media.save()
        return redirect(self.get_success_url())


def medias_of_movie(request, movie_id):
    movie_medias = movie_models.MovieMedia.objects.filter(movie=movie_id)
    data = serializers.serialize("json", movie_medias)
    return HttpResponse(data, content_type="application/json")


class ShowTimeListView(LoginRequiredMixin, ListView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Show Times"}
    template_name = "dashboard/show_times/show_times_list.html"
    model = movie_models.Movie
    context_object_name = "movies"
    ordering = ["-release_date"]


class ShowTimeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Update Screen Time"}
    model = theater_models.ShowTime
    form_class = forms.ShowTimeForm
    template_name = "dashboard/headless_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show_time_form = self.get_form()
        show_time_form.fields[
            "screen_times"
        ].queryset = theater_models.ScreenTime.objects.filter(
            movie=self.object.movie
        )
        context["form"] = show_time_form
        return context

    def get_success_url(self):
        return reverse_lazy("dashboard.formclose")


class ShowTimeDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = movie_models.Movie
    template_name = "dashboard/show_times/show_times_detail.html"
    extra_context = {"page_title": "Movie Show Time"}
    form_class = forms.ShowTimeForm
    slug_field = "pk"
    slug_url_kwarg = "movie_id"

    def get_success_url(self):
        return reverse(
            "dashboard.show_times.details", kwargs={"movie_id": self.object.pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        media_form = self.get_form()
        media_form.fields["movie"].initial = self.object.pk
        # Only showing the screen times associated with the movie
        media_form.fields[
            "screen_times"
        ].queryset = theater_models.ScreenTime.objects.filter(movie=self.object)
        context["form"] = media_form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            # Has some bug form resubmission occur in reload on invalid form
            return self.form_invalid(form)

    def form_valid(self, form):
        show_time = form.save(commit=False)
        show_time.save()
        return redirect(self.get_success_url())


class ScreenTimeCreateView(LoginRequiredMixin, CreateView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "New Screen Time"}
    model = theater_models.ScreenTime
    form_class = forms.ScreenTimeForm
    template_name = "dashboard/show_times/headless_form.html"


class HeadLessFormCloseView(LoginRequiredMixin, TemplateView):
    login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Movie Medias"}
    template_name = "dashboard/headless_form_close.html"
