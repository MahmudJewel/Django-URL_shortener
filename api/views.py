from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import ShortUrlSerializer
from urlShortener.models import ShortURLS
# Create your views here.

# create & retrieve api

class CreateUrls(generics.CreateAPIView):
    serializer_class = ShortUrlSerializer
    queryset = ShortURLS.objects.all()
    # permission_classes = [ AllowAny, ]
    authentication_classes = [JWTAuthentication,]

class AllUrls(generics.ListAPIView):
    queryset = ShortURLS.objects.all()
    serializer_class = ShortUrlSerializer
    paginate_by = 10
    permission_classes = [IsAdminUser, ]
    
