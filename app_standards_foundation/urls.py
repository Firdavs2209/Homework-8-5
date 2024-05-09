from .views import StandardModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'standards', StandardModelViewSet, basename='standards')

urlpatterns = router.urls
