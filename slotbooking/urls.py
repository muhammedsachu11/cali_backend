from django.urls import include, path
from rest_framework import routers
from .views import SlotViewSet


router = routers.DefaultRouter()
router.register(r'slot-list', SlotViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
