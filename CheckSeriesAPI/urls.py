from django.contrib import admin
from django.urls import path

from CSeries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ws/tvshow', views.get_tv_show),
    path('ws/tvshows', views.get_all_tv_shows),
    path('ws/followtvshow', views.follow_tv_show),
    path('ws/updatetvshow', views.update_tv_show),
    path('ws/unfollowtvshow/<int:id>', views.unfollow_tv_show),

    path('ws/checkepisode', views.check_episode),
    path('ws/uncheckepisode/<int:id>', views.uncheck_episode),
    path('ws/episodes', views.get_all_episodes),

    path('ws/favoritetvshow', views.favorite_tv_show),
    path('ws/unfavoritetvshow/<int:id>', views.unfavorite_tv_show),
    path('ws/favoritetvshows', views.get_all_favorite_tv_shows),

    path('authenticate', views.CustomAuthToken.as_view()),
    path('signup', views.sign_up)

]
