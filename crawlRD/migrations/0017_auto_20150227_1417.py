# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0016_auto_20150227_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reddit',
            name='tid',
            field=models.TextField(unique=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='redditcsvcat',
            name='tid',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
