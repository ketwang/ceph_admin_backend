# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('api', models.URLField()),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cluster',
            },
        ),
        migrations.CreateModel(
            name='ClusterCapacity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.FloatField()),
                ('used', models.FloatField()),
                ('objectsNum', models.IntegerField()),
                ('status', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cluster', models.ForeignKey(to='common_models.Cluster')),
            ],
            options={
                'db_table': 'cluster_capacity',
            },
        ),
        migrations.CreateModel(
            name='Osd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('osd_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comeFrom', models.CharField(max_length=3, choices=[(b'CMD', b'pool created by command'), (b'WEB', b'pool created by web page')])),
                ('cluster', models.ForeignKey(to='common_models.Cluster')),
            ],
            options={
                'db_table': 'osd',
            },
        ),
        migrations.CreateModel(
            name='OsdCapacity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crush_weight', models.FloatField()),
                ('reweight', models.FloatField()),
                ('kb_avail', models.IntegerField()),
                ('kb_used', models.IntegerField()),
                ('kb', models.IntegerField()),
                ('pgs', models.IntegerField()),
                ('utilization', models.FloatField()),
                ('osd', models.ForeignKey(to='common_models.Osd')),
            ],
            options={
                'db_table': 'osd_capacity',
            },
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('pool_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comeFrom', models.CharField(max_length=3, choices=[(b'CMD', b'pool created by command'), (b'WEB', b'pool created by web page')])),
                ('cluster', models.ForeignKey(to='common_models.Cluster')),
            ],
            options={
                'db_table': 'pool',
            },
        ),
        migrations.CreateModel(
            name='PoolCapacity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bytes_used', models.IntegerField()),
                ('max_avail', models.IntegerField()),
                ('objectsNum', models.IntegerField()),
                ('quota_objects', models.IntegerField()),
                ('quota_bytes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pool', models.ForeignKey(to='common_models.Pool')),
            ],
            options={
                'db_table': 'pool_capacity',
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('idc', models.CharField(max_length=30)),
                ('room', models.CharField(max_length=30)),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('cluster', models.ForeignKey(to='common_models.Cluster')),
            ],
            options={
                'db_table': 'rack',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=10)),
                ('manufacture', models.CharField(max_length=10)),
                ('server_model', models.CharField(max_length=20)),
                ('ip', models.IPAddressField()),
                ('admin_ip', models.IPAddressField()),
                ('rack', models.ForeignKey(to='common_models.Rack')),
            ],
            options={
                'db_table': 'server',
            },
        ),
    ]
