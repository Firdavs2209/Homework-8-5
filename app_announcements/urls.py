from django.urls import path
from .views import AnnouncementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('announcements', AnnouncementViewSet)


urlpatterns = router.urls





