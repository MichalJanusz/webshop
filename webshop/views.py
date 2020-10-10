from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import View

from webshop.forms import LoginForm


# Create your views here.


class MainView(View):
    def get(self, request):
        return render(request, 'webshop/index.html')


class LogInView(LoginView):
    template_name = 'webshop/login.html'
    authentication_form = LoginForm


class LogOutView(LogoutView):
    pass
