from datetime import date, timedelta
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from movie.models import Movie
from .forms import CommentForm
from django.shortcuts import redirect


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


class UserDashboardView(TemplateView):
    # login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Dashboard"}
    template_name = "frontend/profile/dashboard.html"


class UserTicketView(TemplateView):
    # login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Tickets"}
    template_name = "frontend/profile/tickets.html"


class UserReviewView(TemplateView):
    # login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Reviews"}
    template_name = "frontend/profile/reviews.html"


class UserEditProfileView(TemplateView):
    # login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Edit Profile"}
    template_name = "frontend/profile/edit.html"


class UserChangePasswordView(TemplateView):
    # login_url = "/admin/dashboard/login"
    extra_context = {"page_title": "Change Password"}
    template_name = "frontend/profile/password.html"

