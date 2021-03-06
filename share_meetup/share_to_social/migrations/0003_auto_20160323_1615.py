# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('share_to_social', '0002_profile_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.DecimalField(decimal_places=0, max_digits=20, null=True)),
                ('oauth_token', models.CharField(max_length=200)),
                ('oauth_secret', models.CharField(max_length=200)),
                ('twitter_username', models.CharField(max_length=200, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
