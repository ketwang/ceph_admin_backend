# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crush',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crush_id', models.IntegerField()),
                ('type', models.CharField(max_length=25)),
                ('type_id', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('children', models.CharField(max_length=100)),
                ('crush_weight', models.FloatField(default=0.0)),
                ('reweight', models.FloatField(default=0.0)),
                ('primary_affinity', models.FloatField(default=0.0)),
                ('depth', models.IntegerField(default=0)),
                ('exists', models.IntegerField(default=0)),
                ('cluster', models.ForeignKey(to='common_models.Cluster')),
            ],
        ),
    ]
