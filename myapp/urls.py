from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('product/', views.Products.as_view() , name='product-list'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product/delete/<int:pk>/', views.ProductDelete.as_view(), name='product-delete'),
    path('users/', views.UserList.as_view(), name='users-list'),
    path('logout/', auth_views.LoginView.as_view(), name='logout-user')
]