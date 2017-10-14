from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.edit import CreateView

from .forms import SignupForm

# Create your views here.

class SignupFormView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL

class LoginView(AuthLoginView):
    pass

@login_required
def profile_detail(request):
    return render(request, 'accounts/profile_detail.html')


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup_form.html', {
#         'form' : form
#     })