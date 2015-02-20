# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0006_redditpage_rdfullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redditpage',
            old_name='rdLiFirst',
            new_name='rdComments',
        ),
    ]
