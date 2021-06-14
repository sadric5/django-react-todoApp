from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home-page'),
    path('task/', TodoLists.as_view(), name='task-list'),
    path('tasks/', AllTaks.as_view(), name='all-task-list'),
    path('tasks/<str:completions>', TodoList.as_view(), name='list_tasks'),
    path('task/<int:pk>', TaskUpdateDelete.as_view(), name='update-delete'),
]
