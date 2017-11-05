# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0008_auto_20171027_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='OsdProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_ratio', models.FloatField()),
                ('backfillfull_ratio', models.FloatField()),
                ('nearfull_ratio', models.FloatField()),
                ('pool_max', models.IntegerField()),
                ('max_osd', models.IntegerField()),
                ('require_min_compat_client', models.CharField(max_length=20)),
                ('min_compat_client', models.CharField(max_length=20)),
                ('min_compat_client_version', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'osd_property',
            },
        ),
        migrations.RenameField(
            model_name='pool',
            old_name='name',
            new_name='pool_name',
        ),
        migrations.AddField(
            model_name='pool',
            name='crash_replay_interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pool',
            name='min_size',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='pool',
            name='pg_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pool',
            name='pg_placement_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pool',
            name='quota_max_bytes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pool',
            name='quota_max_objects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pool',
            name='rule',
            field=models.ForeignKey(to='common_models.Rule', null=True),
        ),
        migrations.AddField(
            model_name='pool',
            name='size',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pool',
            name='tier_pool',
            field=models.ForeignKey(to='common_models.Pool', null=True),
        ),
        migrations.AddField(
            model_name='pool',
            name='type',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
