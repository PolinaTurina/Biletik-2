from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *

#добавляет темы на форме
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

#добавляет комментарии с картинкой и без ПОД темой
def tema_detail_view(request, tema_pk):
    tema = Tema.objects.get(pk=tema_pk)

    if request.method == "POST":
        form = OtvetForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            otvet = form.save(commit=False)
            otvet.tema = tema
            otvet.save()
            form = OtvetForm()
            return redirect(request.path)
    else:
        form = OtvetForm()

    otvets = Otvet.objects.filter(tema=tema)

    context = {'tema_detail': tema, 'otvets': otvets, 'otvet_form': form}
    return render(request, 'forum_app/tema_detail.html', context)