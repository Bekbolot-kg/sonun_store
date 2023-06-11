from django.urls import path
from . import views


urlpatterns = [
    path('product_list/', views.ProductListView.as_view(), name='product list'),
    path('product_det/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    ]