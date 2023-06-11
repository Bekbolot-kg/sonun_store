from django.urls import path
from . import views

app_name = 'cloth'

urlpatterns = [
    path('tag1/', views.Tag1ClothesView.as_view(), name='tag1_clothes'),
    path('tag2/', views.Tag2ClothesView.as_view(), name='tag2_clothes'),
    path('tag3/', views.Tag3ClothesView.as_view(), name='tag3_clothes'),
    path('tag4/', views.Tag4ClothesView.as_view(), name='tag4_clothes'),
    path('all/', views.AllClothesView.as_view(), name='all_clothes'),
    path('create-order/', views.CreateOrderView.as_view(), name='create_order'),
]