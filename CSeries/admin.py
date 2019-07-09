from django.contrib import admin

# Register your models here.
from CSeries.models import TVShow, Season, Episode, Favorites

admin.site.register(TVShow)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Favorites)