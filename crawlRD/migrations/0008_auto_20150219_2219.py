# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0007_auto_20150219_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditpage',
            name='rdVote',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='redditpage',
            name='rdComments',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='redditpage',
            name='rdFullName',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
