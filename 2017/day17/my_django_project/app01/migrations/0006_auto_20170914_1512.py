# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_userinfo_admin_column'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '未注册用户')], default=2),
            preserve_default=False,
        ),
    ]