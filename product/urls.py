from django.urls import path
from .views import ProductListView, TypeListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product"),
    path("products/type/", TypeListView.as_view(), name="type"),
]
