from .models import BuildingModel
from .serializers import BuildingSerializer
from rest_framework import viewsets
from .permissions import IsAuthenticatedOrReadOnly


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = BuildingModel.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = BuildingModel.objects.all()
        serializer = BuildingSerializer
