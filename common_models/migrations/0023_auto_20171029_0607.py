# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0022_auto_20171029_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poolcapacity',
            old_name='quota_bytes',
            new_name='kb_used',
        ),
        migrations.RemoveField(
            model_name='poolcapacity',
            name='quota_objects',
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
