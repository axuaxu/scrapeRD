# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0008_auto_20150219_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditpage',
            name='rdLink',
            field=models.CharField(default='wikipedia.org', max_length=300),
            preserve_default=False,
        ),
    ]
