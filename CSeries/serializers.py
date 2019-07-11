from rest_framework import serializers

from CSeries.models import TVShow, Episode, Favorites


class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('id', 'name', 'original_name', 'overview', 'original_language', 'first_air_date')


class FollowingTVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('show_id', 'user', 'date')


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'air_date', 'episode_number', 'name', 'overview', 'season_number')


class CheckedEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'episode_id', 'number', 'user')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'tv_show', 'user')


