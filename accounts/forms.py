from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
    sns = forms.URLField()
    address = forms.CharField()

    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            sns=self.cleaned_data['sns'],
            address=self.cleaned_data['address'],
        )
        return user


