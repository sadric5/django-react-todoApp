from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home-page'),
    path('tasks/', TodoLists.as_view(), name='task-list'),
    path('tasks/<str:completions>', TodoList.as_view(), name='list_tasks'),
]
