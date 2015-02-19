# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0002_auto_20150218_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditpage',
            name='rdDateTime',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
