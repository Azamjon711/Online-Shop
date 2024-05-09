from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view =  get_schema_view(
    openapi.Info(
        title="Online Shop API",
        default_version="v1",
        description="Demo Online Shop API",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="demo@gmail.com"),
        license=openapi.License(name="demo service license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny,]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("product.urls")),
    path("", include("users.urls")),
    path("", include("client.urls")),
    path("api/music/", include("music.urls")),
    path("api/client/", include("clientapi.urls")),
    path("api/product/", include("productapi.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
