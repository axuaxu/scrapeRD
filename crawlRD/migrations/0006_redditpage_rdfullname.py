# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0005_auto_20150218_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditpage',
            name='rdFullName',
            field=models.CharField(default=b'null', max_length=50),
            preserve_default=True,
        ),
    ]
