from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Todo
from .serializers import TodoSerializer
import datetime
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.

class TaskUpdateDelete(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



def addAuthor(data):
        for todo in data:
            todo['author']= User.objects.get(id=todo['author']).username

def home(request):
    # print(request.session)
    todo_lis = Todo.objects.all().filter(completed= False)
    listOfTaks = {}
    for item in todo_lis:
        if item.completed:
            my_time = datetime.datetime.strftime(item.create_at, '%B %d %Y at %H:%M %p')
            elements = item.title, item.description, item.create_at, my_time
            listOfTaks[item.id]=elements
    return JsonResponse(listOfTaks)

class TodoLists(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class AllTaks(APIView):
    def get(self,request):
        allTaks = Todo.objects.all()
        data = TodoSerializer(allTaks, many = True).data
        addAuthor(data)
        return Response(data)
    # def post(self, request):
    #     print(request)

class TodoList(APIView):
    
    def get(self, request, completions):
        if completions.lower()=='true':
            todoComplete = Todo.objects.all().filter(completed = True)
            data = TodoSerializer(todoComplete, many = True).data
            #add the author name
            addAuthor(data)

            return Response(data)
        elif completions.lower()=='false':
            todoComplete = Todo.objects.all().filter(completed = False)
            data = TodoSerializer(todoComplete, many = True).data
            #adding the author name
            addAuthor(data)
            return Response(data)
        else:
            raise Http404("Bad request!")