from django.urls import path
from forum_app.views import *

app_name = 'forum_app'

urlpatterns = [
    path('tema_list/', TemaListView.as_view())
]