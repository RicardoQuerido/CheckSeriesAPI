from datetime import datetime

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.state import User

from .models import TVShow, Episode, Favorites, FollowingTVShow, CheckedEpisode
from CSeries.serializers import TVShowSerializer, EpisodeSerializer, FavoritesSerializer, FollowingTVShowSerializer


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

@api_view(['POST'])
def follow_tv_show(request):
    if not TVShow.objects.filter(id=request.data['show']['id']):
        serializer = TVShowSerializer(data=request.data['show'])
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    tv_show = TVShow.objects.get(id=request.data['show']['id'])

    if FollowingTVShow.objects.filter(tv_show=tv_show, user=request.data['username']):
        FollowingTVShow.objects.get(tv_show=tv_show, user=request.data['username']).delete()
    else:
        FollowingTVShow(tv_show=tv_show, user=request.data['username'], date=datetime.now().strftime('%Y-%m-%d'), episodes_seen=0).save()
    return Response(request.data['show'], status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_tv_show(request):
    try:
        tv_show = TVShow.objects.get(id=request.GET['show'])
    except TVShow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if FollowingTVShow.objects.filter(tv_show=tv_show, user=request.GET['username']):
        return Response("following", status=status.HTTP_200_OK)
    return Response("not following", status=status.HTTP_200_OK)


@api_view(['GET'])
def get_followed_tv_shows(request):
    tv_shows_user = FollowingTVShow.objects.filter(user=request.GET['username'])
    serializer = FollowingTVShowSerializer(tv_shows_user, many=True)
    print(tv_shows_user)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ------------------------------------------------- EPISODES
@api_view(['POST'])
def check_episode(request):
    if not Episode.objects.filter(id=request.data['episode']['id']):
        serializer = EpisodeSerializer(data=request.data['episode'])
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    episode = Episode.objects.get(id=request.data['episode']['id'])

    if CheckedEpisode.objects.filter(episode=episode, user=request.data['username']):
        CheckedEpisode.objects.get(episode=episode, user=request.data['username']).delete()
    else:
        CheckedEpisode(episode=episode, user=request.data['username'], date=datetime.now().strftime('%Y-%m-%d')).save()
    return Response(request.data['episode'], status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_episode(request):
    try:
        episode = Episode.objects.get(id=request.GET['episode'])
    except Episode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if CheckedEpisode.objects.filter(episode=episode, user=request.GET['username']):
        return Response("checked", status=status.HTTP_200_OK)
    return Response("unchecked", status=status.HTTP_200_OK)


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
