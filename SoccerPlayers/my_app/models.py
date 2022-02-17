from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


#
class Players(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(blank=True)
    position = models.CharField(max_length=20, blank=True)
    salary = models.CharField(max_length=20, blank=True)
    team = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(blank=True)
    url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.last_name


class Teams(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    League = models.CharField(max_length=20, blank=True)
    coach_name = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(blank=True, max_length=255)
    url = models.URLField(max_length=255, blank=True)
    slug = models.SlugField(default=country)

    def __str__(self):
        return self.city
