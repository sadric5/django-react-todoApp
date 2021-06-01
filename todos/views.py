from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Todo

# Create your views here.

def home(request):
    # print(request.session)
    todo_lis = Todo.objects.all()
    listOfTaks = {}
    for item in todo_lis:
        if item.completed:
            elements = (item.title, item.description, item.create_at, item.completed)
            listOfTaks[item.id]=elements
    return JsonResponse(listOfTaks)
