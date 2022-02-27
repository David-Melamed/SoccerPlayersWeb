import datetime

from django.db import models
from datetime import date, timedelta


class Teams(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    country = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    League = models.CharField(max_length=20, blank=True)
    coach_name = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(blank=True, max_length=255)
    url = models.URLField(max_length=255, blank=True)
    slug = models.SlugField(default=country)

    def __str__(self):
        return self.name


class Positions(models.Model):
    role = models.CharField(max_length=100, primary_key=True)
    position = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.role


class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=100)
    start_date = models.DateTimeField(blank=True, default="None")
    role = models.ForeignKey(Positions, on_delete=models.CASCADE)
    salary = models.CharField(max_length=20, blank=True, default="None")
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, default="https://icon-library.com/images/2018/2503231_sharks-player-profile-silhouette-hd-png-download.png")
    url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.last_name

