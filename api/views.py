from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import ShortUrlSerializer
from urlShortener.models import ShortURLS
# Create your views here.

# create & retrieve api

class CreateUrls(generics.CreateAPIView):
    serializer_class = ShortUrlSerializer
    queryset = ShortURLS.objects.all()

class AllUrls(generics.ListAPIView):
    queryset = ShortURLS.objects.all()
    serializer_class = ShortUrlSerializer
    paginate_by = 10
    
