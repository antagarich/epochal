# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_name', models.TextField(default='')),
                ('age_description', models.TextField(default='')),
                ('age_year', models.SmallIntegerField(default=0)),
                ('age_image', models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'age_images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_name', models.TextField(default='')),
                ('article_body', models.TextField(default='')),
                ('article_date', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0), auto_now_add=True)),
                ('age', models.ForeignKey(blank=True, to='vkrm.Age', null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GreatDiscovery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discovery_name', models.TextField(default='')),
                ('discovery_description', models.TextField(default='')),
                ('discovery_image', models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'disc_images')),
                ('discovery_year', models.SmallIntegerField(default=0)),
                ('age', models.ForeignKey(to='vkrm.Age')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GreatEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.TextField(default='')),
                ('event_description', models.TextField(default='')),
                ('event_image', models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'event_images')),
                ('event_year', models.SmallIntegerField(default=0)),
                ('age', models.ForeignKey(to='vkrm.Age')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GreatPersonality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pers_name', models.TextField(default='')),
                ('pers_description', models.TextField(default='')),
                ('pers_image', models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'pers_images')),
                ('pers_birth_year', models.SmallIntegerField(default=0)),
                ('pers_death_year', models.SmallIntegerField(default=0)),
                ('pers_metier', models.CharField(default='', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.TextField(default='')),
                ('state_description', models.TextField(default='')),
                ('state_capital', models.TextField(default='')),
                ('state_birth_year', models.SmallIntegerField(default=2015)),
                ('state_image', models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'state_images')),
                ('age', models.ForeignKey(to='vkrm.Age')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wonder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wonder_name', models.TextField(default='')),
                ('wonder_description', models.TextField(default='')),
                ('wonder_image', models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'disc_images')),
                ('wonder_year', models.SmallIntegerField(default=0)),
                ('state', models.ForeignKey(to='vkrm.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='greatpersonality',
            name='state',
            field=models.ForeignKey(to='vkrm.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='discovery',
            field=models.ForeignKey(blank=True, to='vkrm.GreatDiscovery', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='event',
            field=models.ForeignKey(blank=True, to='vkrm.GreatEvent', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='pers',
            field=models.ForeignKey(blank=True, to='vkrm.GreatPersonality', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='state',
            field=models.ForeignKey(blank=True, to='vkrm.State', null=True),
            preserve_default=True,
        ),
    ]
