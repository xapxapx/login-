# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-26 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0024_auto_20190526_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='days_of_emchilgee',
            name='drug',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='drug.Drug_important'),
        ),
    ]
