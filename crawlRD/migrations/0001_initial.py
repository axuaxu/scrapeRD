# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedditPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rdTitle', models.CharField(max_length=500)),
                ('rdDomain', models.CharField(max_length=200)),
                ('rdSubmitter', models.CharField(max_length=300)),
                ('rdLiFirst', models.CharField(max_length=200)),
                ('rdDateTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
