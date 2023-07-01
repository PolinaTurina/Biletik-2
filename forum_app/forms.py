from forum_app.models import *
from django import forms


class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['title']
    title = forms.CharField(max_length=32, label='Название темы:')