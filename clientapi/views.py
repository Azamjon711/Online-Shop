from rest_framework.viewsets import ModelViewSet
from .serializers import AddressSerializer, CitySerializer, CountrySerializer, CustomerSerializer
from client.models import Address, City, Country, Customer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.db.transaction import atomic


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name",]
    pagination_class = LimitOffsetPagination


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name",]
    pagination_class = LimitOffsetPagination


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name",]
    pagination_class = LimitOffsetPagination


class CustomerAPIViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["first_name", "last_name", "email", ]
    pagination_class = LimitOffsetPagination

    @action(detail = True, methods=["GET"])
    def top(self, request, *args, **kwargs):
        customer = self.get_queryset()
        customer = customer.order_by('city')[:3]
        serializer = CustomerSerializer(customer, many=True)
        return Response(data=serializer.data)
