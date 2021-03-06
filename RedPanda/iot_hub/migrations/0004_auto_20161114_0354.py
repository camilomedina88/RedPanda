# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot_hub', '0003_auto_20161114_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('datapoints', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='variable',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AddField(
            model_name='widget',
            name='data_variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_hub.Variable'),
        ),
    ]
