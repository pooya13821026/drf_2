from django.urls import path, include
from . import views
from rest_framework import routers

from .views import UserViewSet, BlogViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
