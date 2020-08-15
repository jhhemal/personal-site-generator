from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm

# Create your views here.

class RegisterView(UserPassesTestMixin, CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')
    permission_denied_message = "You have already Registgered"
    success_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        messages.info(self.request, self.permission_denied_message)
        return redirect('profile')

class AccountLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        messages.success(self.request, f"You have logged in successfully")
        return super().form_valid(form)

        

# def profile(request):
#     return render(request, 'account/profile.html')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'