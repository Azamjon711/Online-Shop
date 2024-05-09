from django.urls import path, include
from .views import TypeAPIViewSet, ProductAPIViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("type", viewset=TypeAPIViewSet)
router.register("product", viewset=ProductAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
