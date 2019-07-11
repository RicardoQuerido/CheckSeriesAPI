from django.db import models


class TVShow(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    original_name = models.CharField(max_length=200)
    overview = models.CharField(max_length=500)
    original_language = models.CharField(max_length=50)
    first_air_date = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class FollowingTVShow(models.Model):
    show_id = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return str(self.show_id)


class Episode(models.Model):
    id = models.IntegerField(primary_key=True)
    air_date = models.CharField(max_length=100)
    episode_number = models.IntegerField()
    name = models.CharField(max_length=200)
    overview = models.CharField(max_length=500)
    season_number = models.IntegerField()

    def __str__(self):
        return str(self.id)


class CheckedEpisode(models.Model):
    episode_id = models.ForeignKey(Episode, on_delete=models.CASCADE)
    number = models.IntegerField()
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.number)


class Favorites(models.Model):
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tv_show)