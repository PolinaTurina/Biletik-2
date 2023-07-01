from django.urls import path
from forum_app.views import *

app_name = 'forum_app'

urlpatterns = [
    path('tema/', tema_list_view , name='tema_list'),
    path('tema_detail/<int:tema_pk>/', tema_detail_view, name='tema_detail'),
]