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


def tema_detail_view(request, tema_pk):
    tema = Tema.objects.get(pk=tema_pk)
    context = {'tema_detail': tema}
    return render(request, 'forum_app/tema_detail.html', context)