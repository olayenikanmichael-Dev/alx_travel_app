from django.urls import path, include
from rest_framework import routers
from .views import ListingViewSet

router = routers.DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listings')

urlpatterns = [
    path('', include(router.urls)),
]
