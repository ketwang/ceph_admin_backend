# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0028_auto_20171030_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crush',
            old_name='children',
            new_name='children_list',
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
