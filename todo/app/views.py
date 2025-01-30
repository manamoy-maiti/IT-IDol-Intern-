from django.shortcuts import render
from app.serializers import todoserializer
from rest_framework import generics
from app.models import todo


from rest_framework.response import Response
# Create your views here.



#read
class ListTodo(generics.ListAPIView):
    queryset = todo.objects.all()
    serializer_class = todoserializer

#update
class updateTodo(generics.UpdateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoserializer    

#create
class CreateTodo(generics.CreateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoserializer

#delete
class deleteTodo(generics.DestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = todoserializer        