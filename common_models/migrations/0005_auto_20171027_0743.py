# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0004_auto_20171027_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crush',
            name='children',
            field=models.CharField(default=b'[]', max_length=100),
        ),
    ]
