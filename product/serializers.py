from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Product
        fields = '__all__' 