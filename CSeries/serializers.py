from rest_framework import serializers

from CSeries.models import TVShow, Season, Episode, Favorites, Comments


class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('id', 'show_id', 'user')


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'season_id', 'number', 'tv_show', 'user')


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'episode', 'number', 'season', 'user')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'tv_show', 'user')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'tv_show', 'user')


