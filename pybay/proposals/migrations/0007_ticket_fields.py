# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-15 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_auto_20170625_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialproposal',
            name='sold_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='ticket_price',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]