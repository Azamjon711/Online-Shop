from rest_framework.viewsets import ModelViewSet
from .serializers import TypeSerializer, ProductSerializer
from product.models import Type, Product
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

class TypeAPIViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name",]
    pagination_class = LimitOffsetPagination


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name", "description", ]
    pagination_class = LimitOffsetPagination



