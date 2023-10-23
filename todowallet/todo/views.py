from django.shortcuts import render
from rest_framework import generics
# Create your views here.


from .models import Category, Task, SubTask
from .serializers import CategorySerializer, TaskSerializer, SubTaskSerializer


class CatCreateList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CatRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CatRetrieveDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskCreateList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskRetrieveDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)