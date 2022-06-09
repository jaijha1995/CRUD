from typing import List
from venv import create
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from api.serializers import ApiSerializer
from api.models import Api


# Create your views here.

class ListApiAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

class CreateApiAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

class UpdateApiAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

class DeleteApiAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Api.objects.all()
    serializer_class = ApiSerializer