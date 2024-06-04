from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ContactViewSet, search
from . import user_forms

router = DefaultRouter()

router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search, name='search'),
    path('login/', user_forms.LoginView.as_view(), name='login'),
    path('user_create/', user_forms.UserCreateView.as_view(), name='user-create'),
    path('user_update/<int:pk>/',
         user_forms.UserUpdateView.as_view(), name='user-update')

]
