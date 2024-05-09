from .views import BuildingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'buildings', BuildingViewSet, basename='buildingnhuhy')


urlpatterns = router.urls