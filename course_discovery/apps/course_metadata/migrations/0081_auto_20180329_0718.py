# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-29 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0080_seat_bulk_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserun',
            name='short_description_override',
            field=models.CharField(blank=True, default=None, help_text="Short description specific for this run of a course. Leave this value blank to default to the parent course's short_description attribute.", max_length=350, null=True),
        ),
    ]
