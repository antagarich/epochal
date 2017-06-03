# coding=utf-8
import datetime
from django.db import models
from django.contrib.auth.models import User


class Age(models.Model):
    age_name = models.TextField(default=u"")
    age_description = models.TextField(default=u"")
    age_year = models.SmallIntegerField(default=0)
    age_image = models.ImageField(upload_to="age_images", default="static/epochal_app/images/6201.jpg")

    def __unicode__(self):
        return self.age_name


class State(models.Model):
    state_name = models.TextField(default=u"")
    state_description = models.TextField(default=u"")
    state_capital = models.TextField(default=u"")
    state_birth_year = models.SmallIntegerField(default=2015)
    state_image = models.ImageField(upload_to="state_images", default="static/epochal_app/images/6201.jpg")
    age = models.ForeignKey(Age)

    def __unicode__(self):
        return self.state_name


class GreatPersonality(models.Model):
    pers_name = models.TextField(default=u"")
    pers_description = models.TextField(default=u"")
    pers_image = models.ImageField(upload_to="pers_images", default="static/epochal_app/images/6201.jpg")
    pers_birth_year = models.SmallIntegerField(default=0)
    pers_death_year = models.SmallIntegerField(default=0)
    pers_metier = models.CharField(max_length=50, default=u"")
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.pers_name


class GreatEvent(models.Model):
    event_name = models.TextField(default=u"")
    event_description = models.TextField(default=u"")
    event_image = models.ImageField(upload_to="event_images", default="static/epochal_app/images/6201.jpg")
    event_year = models.SmallIntegerField(default=0)
    age = models.ForeignKey(Age)

    def __unicode__(self):
        return self.event_name


class GreatDiscovery(models.Model):
    discovery_name = models.TextField(default=u"")
    discovery_description = models.TextField(default=u"")
    discovery_image = models.ImageField(upload_to="disc_images", default="static/epochal_app/images/6201.jpg")
    discovery_year = models.SmallIntegerField(default=0)
    age = models.ForeignKey(Age)

    def __unicode__(self):
        return self.discovery_name


class Article(models.Model):
    article_name = models.TextField(default=u"")
    article_body = models.TextField(default=u"")
    article_date = models.DateTimeField(default=datetime.datetime(2000, 1, 1), auto_now_add=True)
    age = models.ForeignKey(Age, null= True, blank= True)
    state = models.ForeignKey(State, null= True, blank= True)
    pers = models.ForeignKey(GreatPersonality, null= True, blank= True)
    event = models.ForeignKey(GreatEvent, null= True, blank= True)
    discovery = models.ForeignKey(GreatDiscovery, null= True, blank= True)
    author = models.ForeignKey(User, null= True)

    def __unicode__(self):
        return self.article_name


class Wonder(models.Model):
    wonder_name = models.TextField(default=u"")
    wonder_description = models.TextField(default=u"")
    wonder_image = models.ImageField(upload_to="disc_images", default="static/epochal_app/images/6201.jpg")
    wonder_year = models.SmallIntegerField(default=0)
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.wonder_name