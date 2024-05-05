from django.shortcuts import render
from requests import Response
from rest_framework import viewsets

from .models import NewsModel
from .serializers import NewsSerializer
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    def list(self, request):
        queryset = NewsModel.objects.all()
        serializer_class = NewsSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
