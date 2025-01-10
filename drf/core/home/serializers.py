from rest_framework import serializers
from home.models import Person , UserProfile
import re
from django.contrib.auth.models import User 
# from rest_framework.authtoken.models import Token




class people(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'


    def validate(self ,data):
        pattern = r'^[A-ZA-z\s]+$'

        if not re.match(pattern , data['name']):
            raise serializers.ValidationError('name has special characters')
        return data
    



# login page and user page serializer


class loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class Userpageserializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    phone_number = serializers.IntegerField() 


    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("user name already exists")
            
            elif User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError("email already exists")
            
            
        return data

    def create(self , validated_data):
        user = User.objects.create_user(username= validated_data['username'] , email = validated_data['email'], password=validated_data['password'] ) 
        passw = validated_data['password']
        user.set_password(raw_password=passw)
        profile = UserProfile.objects.create(user=user, phone_number=validated_data['phone_number'])
        # token = Token.objects.create(user=user)
        user.save()
       
       
        return user ,profile




       