from django.urls import path
from .views import *

urlpatterns = [
    path('latest_products/', LatestProductsList.as_view()),
    path('products_search/', search),
    path('products/<int:category_id>/<int:product_id>/', ProductDetail.as_view()),
    path('products/<int:pk>/', CategoryDetail.as_view()),
]