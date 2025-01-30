from django.urls import path
from app.views import *


urlpatterns = [
    path('', ListTodo.as_view()),
    path('update/<int:pk>', updateTodo.as_view()),
    path('delete/<int:pk>', deleteTodo.as_view()),
    path('create', CreateTodo.as_view()),



    
]