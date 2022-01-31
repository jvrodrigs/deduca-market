from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.Products.as_view() , name='product-list'),
    path(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product-detail'),
]