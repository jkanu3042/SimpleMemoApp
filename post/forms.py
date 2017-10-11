from django import forms
from .models import Memo

class MemoCreateForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ['author','title', 'content', 'photo']

