from django.shortcuts import render, redirect
from .models import *
from .forms import *


def tema_list_view(request):
    tema = Tema.objects.all()
    
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_app:tema_list')
    else:
        form = TemaForm()

    context = {'tema_list': tema, 'tema_form': form}
    return render (request, 'forum_app/tema_list.html', context)