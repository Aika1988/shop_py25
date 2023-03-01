from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from order.models import *
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderModelViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        queryset = super().get_queryset()  
        queryset = queryset.filter(owner=self.request.user)  
        return queryset