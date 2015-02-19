# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0003_auto_20150218_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditpage',
            name='rdDateTime',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
