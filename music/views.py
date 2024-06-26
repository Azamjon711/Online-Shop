from rest_framework.viewsets import ModelViewSet
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.db.transaction import atomic

class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name",]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["POST"])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        with atomic():
            artist.number_albums += 1
            artist.save()
            return Response(status=status.HTTP_200_OK)


class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title", "artist__name",]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["POST"])
    def count(self, request, *args, **kwargs):
        album = self.get_object()
        with atomic():
            album.count_songs += 1
            album.save()
            return Response(status=status.HTTP_200_OK)


class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["^title", "=album__title", "$album__artist__name"]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["GET"])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with atomic():
            song.listened += 1
            song.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["GET"])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by("-listened")[:3]
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)
