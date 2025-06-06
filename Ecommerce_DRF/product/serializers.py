from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.category_name")

    class Meta:
        model = Product
        fields = ["product_id", "name", "category", "cost", "description"]
        read_only_fields = ["product_id", "date"]


class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
