from home.views import index , person_d , login , Userpage
from django.urls import path 


urlpatterns = [
    path('index/', index),
    path('person/' , person_d),
    path('login/' , login),
    path('userpage/', Userpage)
    
]