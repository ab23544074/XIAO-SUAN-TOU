
from django.contrib import admin
from django.views.generic import TemplateView
from myapp import views
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from myapp.models import Music
from myapp.serializers import *




router = DefaultRouter()
router.register(r'music', views.MusicViewSet)
router.register(r'store', views.StoreViewSet)
router.register(r'Menu', views.MenuViewSet)


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('home/',views.home),
    # path('about/',views.about),
    path('api/', include(router.urls)),
    
    
]




