from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from order.models import *
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import _get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class OrderModelViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):# перед 
        serializer.save(owner=self.request.user)


    def get_queryset(self): # этот тот метод во вьюшке которая говорит с какой именно предметом мы будем работать
        queryset = super().get_queryset()  
        queryset = queryset.filter(owner=self.request.user)  
        return queryset
    

class OrderConfirmAPIView(APIView):
    def get(self, request, code):
        order = _get_object_or_404(Order, activation_code=code)
        if not order.is_confirm:
            order.is_confirm = True
            order.status = 'in_process'
            order.save(update_fields=['is_confirm', 'status'])
            return Response({'message': 'Вы подтвердили заказ!'}, status=status.HTTP_200_OK)
        return Response({'message':'Вы уже подтвердили!'}, status=status.HTTP_400_BAD_REQUEST)
         
