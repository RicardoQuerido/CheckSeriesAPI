from django.db import models


class TVShow(models.Model):
    show_id = models.IntegerField()
    is_finished = models.BooleanField()
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.show_id)


class Season(models.Model):
    season_id = models.IntegerField()
    number = models.IntegerField()
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.number)


class Episode(models.Model):
    episode = models.IntegerField()
    number = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.number)


class Favorites(models.Model):
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tv_show)


'''
class Comments(models.Model):
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tv_show)
'''
