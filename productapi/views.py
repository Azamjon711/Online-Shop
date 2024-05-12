from rest_framework.viewsets import ModelViewSet
from .serializers import TypeSerializer, ProductSerializer
from product.models import Type, Product
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response


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

    @action(detail=False, methods=["GET"])
    def cheap(self, request, *args, **kwargs):
        product = self.get_queryset()
        product = product.order_by("price")[:5]
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)



