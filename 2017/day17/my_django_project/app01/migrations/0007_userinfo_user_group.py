# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20170914_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup'),
        ),
    ]
