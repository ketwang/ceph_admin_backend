# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0006_auto_20171027_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruleset', models.IntegerField()),
                ('rule_id', models.IntegerField()),
                ('rule_name', models.IntegerField(max_length=100)),
                ('type', models.IntegerField()),
                ('max_size', models.IntegerField()),
                ('min_size', models.IntegerField()),
                ('step2', models.CharField(max_length=100)),
                ('step3', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cluster', models.ForeignKey(to='common_models.Cluster')),
                ('step1', models.ForeignKey(to='common_models.Crush')),
            ],
            options={
                'db_table': 'rule',
            },
        ),
    ]
