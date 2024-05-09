from rest_framework import serializers
from product.models import Type, Product

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    type = TypeSerializer

    class Meta:
        model = Product
        fields = "__all__"
