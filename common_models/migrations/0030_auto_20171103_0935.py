# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0029_auto_20171030_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='RBD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField()),
                ('size', models.IntegerField()),
                ('pool', models.ForeignKey(to='common_models.Pool')),
            ],
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
