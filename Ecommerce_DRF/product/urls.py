from django.urls import path
from .views import product_list, messages_list


urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("messages/", messages_list, name="messages"),
]
