from unicodedata import name
from warnings import filters

from myapp.filters import ProductFilter
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer
from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_condition import Or
from django_filters import rest_framework as filters
from django.contrib.auth import logout

# Create your views here.

# Forma de pegar o token:
# POST : /o/token
# basic auth: username : CLIENTE_API / password: CLIENT_SECRET
# body: multipart: username / password / grant_type: password

# Forma de revogar token:
#   POST: /o/revoke_token/
# body FORM: token(ativo) / client_id / client_secret

class UserList(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Products(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['title', 'price']

class ProductDelete(generics.RetrieveDestroyAPIView):
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    queryset = Product.objects.all()
    serializers_class = ProductSerializer

def logoutUser(request):
    logout(request)