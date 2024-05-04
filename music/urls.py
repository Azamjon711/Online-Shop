from django.urls import path, include
from .views import ArtistAPIViewSet, AlbumAPIViewSet, SongAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("artist", viewset=ArtistAPIViewSet)
router.register("album", viewset=AlbumAPIViewSet)
router.register("song", viewset=SongAPIViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", views.obtain_auth_token),
]
