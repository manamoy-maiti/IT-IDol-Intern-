from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path('', views.index, name= 'home'),
    path('services', views.services , name ='service' ),
    path('contact', views.contact_save , name = 'contact' )
]