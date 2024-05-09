from django.urls import path, include
from .views import AddressAPIViewSet, CityAPIViewSet, CountryAPIViewSet, CustomerAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("address", viewset=AddressAPIViewSet)
router.register("city", viewset=CityAPIViewSet)
router.register("country", viewset=CountryAPIViewSet)
router.register("customer", viewset=CustomerAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
