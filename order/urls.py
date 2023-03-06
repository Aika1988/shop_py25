from rest_framework.routers import DefaultRouter
from django.urls import path, include
from order.views import OrderModelViewset, OrderConfirmAPIView

router = DefaultRouter()
router.register('', OrderModelViewset)

urlpatterns = [
    path('confirm/<uuid:code>/', OrderConfirmAPIView.as_view()),
    path('', include(router.urls)),

]