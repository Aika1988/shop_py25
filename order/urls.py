from rest_framework.routers import DefaultRouter
from django.urls import path, include
from order.views import OrderModelViewset

router = DefaultRouter()
router.register('', OrderModelViewset)

urlpatterns = [
    path('', include(router.urls)),

]