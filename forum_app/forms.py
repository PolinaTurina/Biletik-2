from forum_app.models import *
from django import forms


class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['title']
    title = forms.CharField(max_length=32, label='Название темы:')


class OtvetForm(forms.ModelForm):
    class Meta:
        model = Otvet
        fields = ['name', 'text', 'image',]

    name = forms.CharField(max_length=32, label='Ваше имя')
    text = forms.CharField(max_length=200, label='Ваш ответ',
                           widget=forms.Textarea(attrs={'cols':100, 'rows':5, 'placeholder': 'Я напишу...'}))
    image = forms.ImageField(required=False)