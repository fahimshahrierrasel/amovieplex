from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>', views.SingleMovie.as_view(), name='single_movie'),
]