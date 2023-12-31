from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect

class UserListView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = self.request.user.groups.all()
        return context

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'
    next_page = 'home'

def my_logout(request):
    logout(request)
    return redirect('login')
