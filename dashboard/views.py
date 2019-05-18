from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.urls import reverse


class LoginView(LoginView):
    template_name = 'dashboard/auth/login.html'
    redirect_authenticated_user = True
    extra_context = {'page_title': 'Admin Login'}

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('dashboard')


class LogoutView(LogoutView):
    next_page = '/admin/dashboard/login'


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/dashboard/login'
    template_name = "dashboard/index.html"
    extra_context = {'page_title': 'Dashboard'}
