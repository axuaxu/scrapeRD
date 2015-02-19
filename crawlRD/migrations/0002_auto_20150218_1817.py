# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redditpage',
            name='rdTitle',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
