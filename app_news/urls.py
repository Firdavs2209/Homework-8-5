from django.urls import path
from .views import NewsViewSet, StandardsViewSet, UnitsViewSet, LeadershipViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')
router.register(r'standards', StandardsViewSet, basename='standards')
router.register(r'units', UnitsViewSet, basename='units')
router.register(r'leadership', LeadershipViewSet, basename='leadership')


urlpatterns = router.urls

