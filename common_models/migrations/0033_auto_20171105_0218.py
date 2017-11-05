# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0032_auto_20171104_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbd',
            name='block_name_prefix',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rbd',
            name='num_objs',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rbd',
            name='obj_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rbd',
            name='parent',
            field=models.ForeignKey(to='common_models.RBD', null=True),
        ),
        migrations.AlterField(
            model_name='rbd',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='rbd',
            name='pool',
            field=models.ForeignKey(related_name='images', to='common_models.Pool'),
        ),
        migrations.AlterField(
            model_name='rbd',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
