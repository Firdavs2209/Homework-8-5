from .views import ConnectionViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'connection', ConnectionViewSet, basename='Connection')


urlpatterns = router.urls