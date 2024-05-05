from django.shortcuts import render
from requests import Response

from rest_framework import viewsets
from .models import Announcement
from .serializers import AnnouncementSerializer
from .permissions import IsAuthenticatedOrReadOnly


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def list(self, request):
        queryset = Announcement.objects.all()
        serializer = AnnouncementSerializer
        permission_classes = (IsAuthenticatedOrReadOnly,)
