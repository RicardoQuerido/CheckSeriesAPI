from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from CSeries.models import TVShow, Episode, Season, Favorites
from CSeries.serializers import TVShowSerializer, EpisodeSerializer, SeasonSerializer, FavoritesSerializer


# ------------------------------------------------- TV SHOWS
@api_view(['GET'])
def get_tv_show(request):  # provavelmente desnecessário
    id = int(request.GET['id'])
    try:
        tv_show = TVShow.objects.get(id=id)
    except TVShow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TVShowSerializer(tv_show)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_tv_shows(request):
    # Isto deveria ser um filter por user?
    tv_shows = TVShow.objects.all()
    serializer = TVShowSerializer(tv_shows, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def follow_tv_show(request):
    serializer = TVShowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_tv_show(request):  # provavelmente desnecessário
    id = int(request.GET['id'])
    try:
        tv_show = TVShow.objects.get(id=id)
    except TVShow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TVShowSerializer(tv_show, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def unfollow_tv_show(request, id):
    try:
        tv_show = TVShow.objects.get(id=id)
    except TVShow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # provavelmente tenho de apagar todos os episodios e seasons marcados tambem
    tv_show.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------------------- SEASONS
# provavelmente desnecessário: possivelmente só é preciso guardar os episódios marcados;
@api_view(['POST'])
def check_season(request):
    serializer = SeasonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def uncheck_season(request, id):
    try:
        season = Season.objects.get(id=id)
    except Season.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    season.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------------------- EPISODES
@api_view(['POST'])
def check_episode(request):
    serializer = EpisodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def uncheck_episode(request, id):
    try:
        episode = Episode.objects.get(id=id)
    except Episode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    episode.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_episodes(request):
    # Isto deveria ser um filter por user?
    checked_episodes = Episode.objects.all()
    serializer = EpisodeSerializer(checked_episodes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ------------------------------------------------- FAVORITES
@api_view(['POST'])
def favorite_tv_show(request):
    serializer = FavoritesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def unfavorite_tv_show(request, id):
    try:
        favorite = Favorites.objects.get(id=id)
    except Favorites.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    favorite.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_favorite_tv_shows(request):
    # Isto deveria ser um filter por user?
    favorites = Episode.objects.all()
    serializer = EpisodeSerializer(favorites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
