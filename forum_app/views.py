from django.shortcuts import render
from django.views.generic import ListView
from forum_app.models import *


class TemaListView(ListView):
    model = Tema
    template_name = 'forum_app/tema_list.html'
    context_object_name = 'tema_list'
