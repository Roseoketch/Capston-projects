# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('child', '0002_organization_time_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]