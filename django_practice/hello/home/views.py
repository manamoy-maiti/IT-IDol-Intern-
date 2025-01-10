from django.shortcuts import render , HttpResponse
from home.models import contact

# Create your views here.

def index(request):
    return render(request ,'index.html')

def services(request):
    return HttpResponse("this is services page ")

def contact_save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        print("name > ", name)
        Contact_details = contact(name= name , email= email , phone_number = phone_number )
        Contact_details.save()



    return render(request, 'contact.html' )