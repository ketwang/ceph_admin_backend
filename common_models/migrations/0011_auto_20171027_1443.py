# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0010_auto_20171027_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osd',
            name='name',
        ),
        migrations.AddField(
            model_name='osd',
            name='_in',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='osd',
            name='cluster_addr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='osd',
            name='heartbeat_back_addr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='osd',
            name='heartbeat_front_addr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='osd',
            name='public_addr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='osd',
            name='up',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='osd',
            name='uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='osd',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
