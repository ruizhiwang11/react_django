from django.db.models.query import QuerySet
from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics, serializers
from .serializers import RoomSerializer
from .models import Room
# Create your views here.



# def main(request):
#     return HttpResponse("Hello")

class RoomView(generics.ListAPIView):
    # must have query set attribute
    queryset = Room.objects.all()
    serializer_class = RoomSerializer