from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.state import User

from .models import TVShow, Episode, Favorites
from CSeries.serializers import TVShowSerializer, EpisodeSerializer, FavoritesSerializer

# ------------------------------------------------- Authentication
@api_view(['POST'])
def sign_up(request):
    print('aqui')
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create(username=username, password=password)
    user.set_password(user.password)
    user.save()
    return Response(status=status.HTTP_201_CREATED)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'username': user.username,
            'token': token.key
        })

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
