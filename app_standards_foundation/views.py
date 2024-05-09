from rest_framework import viewsets,pagination
from .models import StandardModel
from .serializers import StandardModelSerializer
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters


class StandardModelPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StandardModelViewSet(viewsets.ModelViewSet):
    queryset = StandardModel.objects.all()
    serializer_class = StandardModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'number']
    pagination_class = StandardModelPagination

    def list(self, request, *args, **kwargs):
        queryset = StandardModel.objects.all()
        serializer = StandardModelSerializer(queryset, many=True)
        permission_classes = [IsAuthenticatedOrReadOnly]



