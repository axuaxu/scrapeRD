# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlRD', '0009_redditpage_rdlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedditCSV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_utc', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('domain', models.CharField(max_length=100)),
                ('tid', models.CharField(max_length=30)),
                ('title', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('ups', models.IntegerField()),
                ('downs', models.IntegerField()),
                ('num_comments', models.IntegerField()),
                ('permalink', models.CharField(max_length=300)),
                ('selftext', models.CharField(max_length=200)),
                ('link_flair_text', models.CharField(max_length=300)),
                ('over_18', models.BooleanField()),
                ('thumbnail', models.CharField(max_length=30)),
                ('subreddit_id', models.CharField(max_length=50)),
                ('edited', models.BooleanField()),
                ('link_flair_css_class', models.CharField(max_length=30)),
                ('author_flair_css_class', models.CharField(max_length=30)),
                ('is_self', models.BooleanField()),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=300)),
                ('distinguished', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
