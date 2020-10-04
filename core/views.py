from random import randint
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, views, status
from rest_framework.response import Response
from .serializers import *
from .models import *


class HomeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # + permission


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoCreateSerializer


class AddToDoView(generics.CreateAPIView):
    serializer_class = ToDoCreateSerializer

    def post(self, request, *args, **kwargs):
        url = randint(1, 10 ** 6)
        while ToDoList.objects.filter(url=url).exists():
            url = randint(1, 10 ** 6)
        todo_list = ToDoList(url=url)
        todo_list.save()

        # create todo obj и присоед-е его к todo_list
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        headers = self.get_success_headers(serializer.data)
        todo.todo_list = todo_list
        todo.save()
        dic = serializer.data
        dic["url"] = url

        return Response(dic, status=status.HTTP_201_CREATED, headers=headers)


class SetToDoListCodeView:
    pass


class ToDoAPIView(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        url = self.kwargs["url"]
        todo_list = ToDo.objects.filter(todo_list__url=url)
        return todo_list


class AddTodoToListView(generics.CreateAPIView):
    serializer_class = ToDoCreateSerializer

    def post(self, request, *args, **kwargs):
        url = self.kwargs["url"]
        todo_list = ToDoList.objects.get(url=url)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        headers = self.get_success_headers(serializer.data)
        todo.todo_list = todo_list
        todo.save()
        dic = serializer.data
        dic["url"] = url

        return Response(dic, status=status.HTTP_201_CREATED, headers=headers)


class ToDoListSetCodeView(generics.UpdateAPIView):
    serializer_class = ToDoListCodeSerializer
    lookup_field = "url" # поле по которому получает todolist

    def get_queryset(self):
        return ToDoList.objects.filter(url=self.kwargs["url"])

    # def put(self, request, *args, **kwargs):
    #     url = self.kwargs["url"]
    #     todo_list = ToDoList.objects.get(url=url)
