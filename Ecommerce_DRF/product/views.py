from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .simple_serializers import Message


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def messages_list(request):
    message = Message(email="leila@example.com", content="foo bar")
    serializer = MessageSerializer(message)

    return Response(serializer.data)
