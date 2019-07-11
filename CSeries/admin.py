from django.contrib import admin

# Register your models here.
from CSeries.models import TVShow, Episode, Favorites, FollowingTVShow, CheckedEpisode

admin.site.register(FollowingTVShow)
admin.site.register(TVShow)
admin.site.register(CheckedEpisode)
admin.site.register(Episode)
admin.site.register(Favorites)