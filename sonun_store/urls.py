from django.urls import path
from . import views


urlpatterns = [
    path('hi/', views.sonun_view, name='hi'),
    path('', views.sonun_store_view, name='sonun_store'),
    path('product_detail/<int:id>/', views.product_detail_view, name='product_detail'),
    path('product_detail/<int:id>/delete/', views.delete_product_view, name='delete_product'),
    path('product_detail/<int:id>/update/', views.update_product_view, name='update_productt'),
    path('add-product/', views.create_product_view, name='create_product'),
    path('add-review/', views.review_product_view, name='review_product'),

]