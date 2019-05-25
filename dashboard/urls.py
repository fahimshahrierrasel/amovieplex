from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path("login", views.LoginView.as_view(), name="dashboard.login"),
    path("logout", views.LogoutView.as_view(), name="dashboard.logout"),
    # Dashboard
    path("", views.DashboardView.as_view(), name="dashboard.index"),
    # Movies
    path("movies/", views.MovieListView.as_view(), name="dashboard.movie.list"),
    path(
        "movies/<int:pk>",
        views.MovieDetailView.as_view(),
        name="dashboard.movie.detail",
    ),
    path(
        "movies/create",
        views.MovieCreateView.as_view(),
        name="dashboard.movie.create",
    ),
    path(
        "movies/<int:pk>/edit",
        views.MovieUpdateView.as_view(),
        name="dashboard.movie.edit",
    ),
    # Movie Medias
    path(
        "movie-medias",
        views.MovieMediaView.as_view(),
        name="dashboard.movie_medias",
    ),
    path(
        "movie-medias/<int:movie_id>",
        views.medias_of_movie,
        name="dashboard.medias"
    )
]
