# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0005_auto_20171027_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='crush',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 27, 8, 16, 26, 188306, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crush',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 27, 8, 16, 43, 670391, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
