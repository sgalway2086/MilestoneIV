from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.shop, name='shop'),
    path('<int:product_id>/', views.view_product, name='view_product'),
    path('add/', views.add_product, name="add_product"),
]
