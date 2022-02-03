from pyexpat import model
from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    
    title = filters.CharFilter(field_name="title")
    price = filters.CharFilter(field_name="price")

    class Meta: 
        model = Product
        fields = '__all__'