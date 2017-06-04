# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vkrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_name', models.CharField(default='', unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_type', models.TextField(default='')),
                ('object_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission_name', models.CharField(default='', unique=True, max_length=100)),
                ('action', models.ForeignKey(to='vkrm.Action')),
                ('object', models.ForeignKey(to='vkrm.Object')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(default='', unique=True, max_length=100)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='permission',
            name='role',
            field=models.ForeignKey(to='vkrm.Role'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='age',
            name='age_image',
            field=models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'age_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='greatdiscovery',
            name='discovery_image',
            field=models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'disc_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='greatevent',
            name='event_image',
            field=models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'event_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='greatpersonality',
            name='pers_image',
            field=models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'pers_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='state',
            name='state_image',
            field=models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'state_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wonder',
            name='wonder_image',
            field=models.ImageField(default=b'static/epochal_app/images/6201.jpg', upload_to=b'disc_images'),
            preserve_default=True,
        ),
    ]
