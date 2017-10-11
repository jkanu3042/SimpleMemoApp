from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import SignupForm

# Create your views here.

@login_required
def profile_detail(request):
    return render(request, 'accounts/profile_detail.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form' : form
    })