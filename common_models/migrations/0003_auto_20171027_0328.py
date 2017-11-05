# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0002_crush'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='crush',
            table='crush_type',
        ),
    ]
