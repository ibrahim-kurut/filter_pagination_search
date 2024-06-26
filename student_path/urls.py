from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PathModelViewSet, StudentModelViewSet


router = DefaultRouter()
router.register('paths', PathModelViewSet)
router.register('students', StudentModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]