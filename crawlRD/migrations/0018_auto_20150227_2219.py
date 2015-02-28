# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0017_auto_20150227_1417'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reddit',
            new_name='RedditPedia',
        ),
    ]
