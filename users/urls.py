from django.urls import path
from .views import (LandingPageView, UserRegisterView, UserLoginView, UserLogOutView, ShopPageView, ShopDetailPageView,
                    ChecOutPageView, CartPageView, TestimonialPageView, ContactPageView)

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("shop/", ShopPageView.as_view(), name="shop"),
    path("shop/cart", CartPageView.as_view(), name="cart"),
    path("shop/checkout", ChecOutPageView.as_view(), name="checkout"),
    path("testimonial/", TestimonialPageView.as_view(), name="testimonial"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("shop/details/", ShopDetailPageView.as_view(), name="shop-details"),
    path("user/register/", UserRegisterView.as_view(), name="register"),
    path("user/login/", UserLoginView.as_view(), name="login"),
    path("user/logout/", UserLogOutView.as_view(), name="logout"),
]
