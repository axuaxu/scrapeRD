# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0018_auto_20150227_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reddit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_utc', models.TextField(blank=True)),
                ('score', models.TextField(blank=True)),
                ('domain', models.TextField(blank=True)),
                ('tid', models.TextField(unique=True, blank=True)),
                ('title', models.TextField(blank=True)),
                ('author', models.TextField(blank=True)),
                ('ups', models.TextField(blank=True)),
                ('downs', models.TextField(blank=True)),
                ('num_comments', models.TextField(blank=True)),
                ('permalink', models.TextField(blank=True)),
                ('selftext', models.TextField(blank=True)),
                ('link_flair_text', models.TextField(blank=True)),
                ('over_18', models.TextField(blank=True)),
                ('thumbnail', models.TextField(blank=True)),
                ('subreddit_id', models.TextField(blank=True)),
                ('edited', models.TextField(blank=True)),
                ('link_flair_css_class', models.TextField(blank=True)),
                ('author_flair_css_class', models.TextField(blank=True)),
                ('is_self', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('distinguished', models.TextField(blank=True)),
                ('catName', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
