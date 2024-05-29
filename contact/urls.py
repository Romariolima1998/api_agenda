from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ContactViewSet

router = DefaultRouter()

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls))
]
