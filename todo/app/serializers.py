from rest_framework import serializers
from app.models import todo


class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        # fields = ('id' , 'Title', 'Description' , 'Date' , 'Completed')
        fields = '__all__'
