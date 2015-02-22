# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0012_redditsub'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditsub',
            name='load',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
