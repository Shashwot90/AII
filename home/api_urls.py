from .api_views import *
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'icategory', ICategoryViewSet)
router.register(r'iprogram', IProgramViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    
]