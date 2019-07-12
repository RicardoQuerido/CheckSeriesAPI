from rest_framework import serializers

from CSeries.models import TVShow, Episode, Favorites, FollowingTVShow, CheckedEpisode


class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('id', 'name', 'original_name', 'overview', 'original_language', 'first_air_date', 'backdrop_path')


class FollowingTVShowSerializer(serializers.ModelSerializer):
    tv_show = TVShowSerializer()

    class Meta:
        model = FollowingTVShow
        fields = ('tv_show', 'user', 'date', 'episodes_seen')


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'air_date', 'episode_number', 'name', 'overview', 'season_number')


class CheckedEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckedEpisode
        fields = ('id', 'episode', 'number', 'user')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'tv_show', 'user')


