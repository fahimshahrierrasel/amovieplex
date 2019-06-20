from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("movie/<int:pk>", views.SingleMovie.as_view(), name="single_movie"),
    path("user/dashboard", views.UserDashboardView.as_view(), name="user_dashboard"),
    path("user/tickets", views.UserTicketView.as_view(), name="user_tickets"),
    path("user/reviews", views.UserReviewView.as_view(), name="user_reviews"),
    path("user/edit-profile", views.UserEditProfileView.as_view(), name="profile_edit"),
    path("user/change-password", views.UserChangePasswordView.as_view(), name="change_password"),
]
