from django.urls import path
from . import views

urlpatterns = [
    path('start_parsing/', views.ParserFormView.as_view(), name='parser'),
    path('film_parsing/', views.FilmListView.as_view(), name='film_list'),
    path('product_parsing/', views.ProductListView.as_view(), name='product_list'),
    path('product_search/', views.Searchs.as_view(), name='search'),

]