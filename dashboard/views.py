from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse, reverse_lazy
from movie import models as movie_models
from . import forms


class LoginView(LoginView):
    template_name = 'dashboard/auth/login.html'
    redirect_authenticated_user = True
    extra_context = {'page_title': 'Admin Login'}

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('dashboard.index')


class LogoutView(LogoutView):
    next_page = '/admin/dashboard/login'


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/dashboard/login'
    extra_context = {'page_title': 'Dashboard'}
    template_name = "dashboard/index.html"


class MovieListView(LoginRequiredMixin, ListView):
    login_url = '/admin/dashboard/login'
    extra_context = {'page_title': 'Movies'}
    template_name = 'dashboard/movies/movie_list.html'
    model = movie_models.Movie
    context_object_name = 'movies'


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = movie_models.Movie
    template_name = 'dashboard/movies/movie_detail.html'
    extra_context = {'page_title': 'Movie Detail'}


class MovieCreateView(LoginRequiredMixin, CreateView):
    login_url = '/admin/dashboard/login'
    extra_context = {'page_title': 'New Movie'}
    model = movie_models.Movie
    form_class = forms.MovieForm
    template_name = 'dashboard/movies/movie_form.html'


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/dashboard/login'
    extra_context = {'page_title': 'Update Movie'}
    model = movie_models.Movie
    form_class = forms.MovieForm
    template_name = 'dashboard/movies/movie_form.html'
    success_url = reverse_lazy('dashboard.movie.list')
