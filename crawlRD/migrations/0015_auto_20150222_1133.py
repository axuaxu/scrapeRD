# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0014_redditcsvcat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redditcsvcat',
            old_name='catNamte',
            new_name='catName',
        ),
    ]
