# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0027_auto_20171030_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clustercapacity',
            name='objectsNum',
        ),
        migrations.RemoveField(
            model_name='clustercapacity',
            name='status',
        ),
        migrations.RemoveField(
            model_name='clustercapacity',
            name='total',
        ),
        migrations.RemoveField(
            model_name='clustercapacity',
            name='used',
        ),
        migrations.AddField(
            model_name='clustercapacity',
            name='total_kb',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='clustercapacity',
            name='total_kb_avail',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='clustercapacity',
            name='total_kb_used',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='clustercapacity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='clustercapacity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
