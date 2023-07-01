from django.urls import path
from forum_app.views import *

app_name = 'forum_app'

urlpatterns = [
    path('tema_list/', tema_list_view , name='tema_list')
]