from datetime import date, timedelta

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import (DetailView)
from django.views.generic.base import TemplateView
from django.views.generic.edit import (FormMixin, FormView)

from movie.models import Movie
from .forms import CommentForm


class IndexView(TemplateView):
    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        all_movies = Movie.objects.all()
        context["movies"] = all_movies
        context["new_in"] = all_movies
        running_shows = []
        today = date.today()
        i = 0
        for show_date in [today + timedelta(x) for x in range(4)]:
            running_shows.append(
                {"show_date": show_date, "movies": all_movies[i:]}
            )
            i = i + 1

        context["running_shows"] = running_shows
        context["up_comming_movies"] = all_movies
        return context


class SingleMovie(FormMixin, DetailView):
    template_name = "frontend/single_movie.html"
    model = Movie
    context_object_name = "movie"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("single_movie", kwargs={"pk": self.object.pk})

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


class UserDashboardView(LoginRequiredMixin, TemplateView):
    login_url = "user_login"
    extra_context = {"page_title": "Dashboard"}
    template_name = "frontend/profile/dashboard.html"


class UserTicketView(LoginRequiredMixin, TemplateView):
    login_url = "user_login"
    extra_context = {"page_title": "Tickets"}
    template_name = "frontend/profile/tickets.html"


class UserReviewView(LoginRequiredMixin, TemplateView):
    login_url = "user_login"
    extra_context = {"page_title": "Reviews"}
    template_name = "frontend/profile/reviews.html"


class UserEditProfileView(LoginRequiredMixin, TemplateView):
    login_url = "user_login"
    extra_context = {"page_title": "Edit Profile"}
    template_name = "frontend/profile/edit.html"


class UserChangePasswordView(LoginRequiredMixin, TemplateView):
    login_url = "user_login"
    extra_context = {"page_title": "Change Password"}
    template_name = "frontend/profile/password.html"


class UserRegistrationView(FormView):
    # redirect_authenticated_user = True
    template_name = "frontend/auth/register.html"
    form_class = UserCreationForm
    extra_context = {"page_title": "User Registration"}
    success_url = "/user/login"

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class UserLoginView(LoginView):
    template_name = "frontend/auth/login.html"
    redirect_authenticated_user = True
    extra_context = {"page_title": "User Login"}

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse("user_dashboard")


class UserLogoutView(LogoutView):
    next_page = "user_login"
