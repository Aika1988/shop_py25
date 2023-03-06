from django.shortcuts import render
from rest_framework import mixins, viewsets
from spam.serializers import ContactSerializer
from spam.models import *
from rest_framework.permissions import IsAuthenticated

class ContactAPIView(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(email=self.request.user)
