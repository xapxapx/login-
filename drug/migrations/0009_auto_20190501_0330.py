# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-30 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0008_auto_20190501_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug_important',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Drug_detail'),
        ),
        migrations.AlterField(
            model_name='drug_important',
            name='shirheg',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
