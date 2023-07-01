from django.contrib import admin
from forum_app.models import *   


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    search_fields = ['title']
    list_filter = ['created_date']

@admin.register(Otvet)
class OtvetAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'created_date']
    search_fields = ['name', 'text']
    list_filter = ['created_date']