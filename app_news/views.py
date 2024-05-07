from django.shortcuts import render
from requests import Response
from rest_framework import viewsets

from .models import NewsModel,StandardsModel,UnitsModel,LeadershipModel
from .serializers import NewsSerializer, StandardsModel, StandardsSerializer,UnitsSerializer,LeadershipSerializer
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    def list(self, request):
        queryset = NewsModel.objects.all()
        serializer_class = NewsSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]



class StandardsViewSet(viewsets.ModelViewSet):
    queryset = StandardsModel.objects.all()
    serializer_class = StandardsModel
    def list(self, request):
        queryset = StandardsModel.objects.all()
        serializer_class = StandardsSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]


class UnitsViewSet(viewsets.ModelViewSet):
    queryset = UnitsModel.objects.all()
    serializer_class = UnitsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = UnitsModel.objects.all()
        serializer_class = UnitsSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]


class LeadershipViewSet(viewsets.ModelViewSet):
    queryset = LeadershipModel.objects.all()
    serializer_class = LeadershipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request):
        queryset = LeadershipModel.objects.all()
        serializer_class = LeadershipSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
        serializer = LeadershipSerializer(queryset, many=True)




