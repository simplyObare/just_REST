from django.urls import path
from .views import (
    product_list,
    messages_list,
    ProductListView,
    ProductDetailsView,
    ProductListMixins,
    ProductDetailsMixins,
)


urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("messages/", messages_list, name="messages"),
    path("class-product-list/", ProductListView.as_view(), name="class-product-list"),
    path(
        "class-product-details/<uuid:product_id>/",
        ProductDetailsView.as_view(),
        name="class-product-details",
    ),
    path("mixinpath/", ProductListMixins.as_view(), name="mixinpath"),
    path(
        "detailsmixinpath/<uuid:product_id>/",
        ProductDetailsMixins.as_view(),
        name="detailsmixinpath",
    ),
]
