from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login', views.LoginView.as_view(), name='dashboard.login'),
    path('logout', views.LogoutView.as_view(), name='dashboard.logout'),
    # Dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),
]
