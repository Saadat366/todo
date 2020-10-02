from django.contrib.auth.models import User # Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "first_name", "last_name"]

class ToDoCreateSerializer(serializers.ModelSerializer):
    url = serializers.IntegerField(required=False)
    class Meta:
        model = ToDo
        fields = ["text", "url"]

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["text", "created"]

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["url"]