from spam.models import *
from rest_framework import serializers 

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'
        

    def create(self, validated_data):
        if Contact.objects.filter(email=validated_data).exists():
            raise serializers.ValidationError('Вы уже подписались!')   
        return super().create(validated_data)