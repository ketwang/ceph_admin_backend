# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0019_auto_20171028_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='osd',
            name='osd_class',
            field=models.CharField(default=b'Non-SSD', max_length=20, choices=[(b'SSD', b'solid state disk'), (b'Non-SSD', b'sas or sata disk')]),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
