# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0021_auto_20171029_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osd',
            name='osd_class',
            field=models.CharField(default=b'sata', max_length=20, choices=[(b'ssd', b'solid state disk'), (b'sata', b'sata disk')]),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
