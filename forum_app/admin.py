from django.contrib import admin
from forum_app.models import *   


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    search_fields = ['title']