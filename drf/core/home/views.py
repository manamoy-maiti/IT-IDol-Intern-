from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from home.models import Person
from home.serializers import people , loginserializer , Userpageserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication , BasicAuthentication



# from rest_framework import viewsets

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token





@api_view(['GET' ,'POST'])
def index(request):
    courses = {
        'course_name' : 'python',
        'course_provider' : 'scaler'
    } 

    if request.method == 'GET':
        print("you hit the get method")
        return Response(courses)

    elif request.method == 'POST':
        print("you hit the post method")    
        data = request.data
        print(data)
        return Response(courses)
    

@api_view(['GET','POST','PATCH','DELETE'])
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  #authentication_classes=[TokenAuthentication]
def person_d(request):
    
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = people(objs , many =True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data 
        serializer = people(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data 
        obj = Person.objects.get(id= data['id'])
        serializer = people(obj, data = data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id= data['id'])
        obj.delete()
        return Response({'message': 'data deleted'})



# login page and user page views  

@api_view(['POST'])
def Userpage(request):
    data = request.data 
    serializer = Userpageserializer(data =data)

    if serializer.is_valid():
        data =serializer.validated_data
        serializer.save()
        return Response({"message : success"})
    
    return Response(serializer.errors)



@api_view(['POST'])
def login(request):
    data = request.data
    serializer = loginserializer(data = data)

    if not serializer.is_valid():
        return Response({"message": "invalid credentials" })
    
    user = authenticate(username = serializer.data["username"] , password = serializer.data["password"])

    token = Token.objects.get_or_create(user=user)
    print(token)

    return Response({"message" : "user logined" , "token": str(token)})

        



# class peopleViewset(viewsets.ModelViewSet):
#     serializer_class = people
#     queryset = Person.objects.all()