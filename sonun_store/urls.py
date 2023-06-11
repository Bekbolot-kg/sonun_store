from django.urls import path
from . import views


urlpatterns = [
    path("", views.SonunStoreView.as_view(), name="sonun_store"),
    path(
        "product_detail/<int:id>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "product_detail/<int:id>/delete/",
        views.DeleteProductview.as_view(),
        name="delete_product",
    ),
    path(
        "product_detail/<int:id>/update/",
        views.UpdateProductView.as_view(),
        name="update_productt",
    ),
    path("add-product/", views.CreateProductView.as_view(), name="create_product"),
    path("add-review/", views.ReviewProductView.as_view(), name="review_product"),
    path("search/", views.Search.as_view(), name="search"),
]
