from django.db import models

# Create your models here.


class RedditPage(models.Model):
    """
      Reddit Page Fields
    """
    rdTitle = models.TextField()
    rdLink = models.CharField(max_length=300)
    rdDomain = models.CharField(max_length=200)
    rdSubmitter = models.CharField(max_length=300)
    rdVote = models.IntegerField()
    rdComments = models.IntegerField()
    rdFullName = models.CharField(max_length=50)
    rdDateTime = models.DateTimeField()


class RedditCSV(models.Model):
    """
      Reddit Page Fields from CSV Files
      created_utc,score,domain,id,title,author,ups,downs,num_comments,permalink,selftext,link_flair_text,over_18,
      thumbnail,subreddit_id,edited,link_flair_css_class,author_flair_css_class,is_self,name,url,distinguished
    """
    created_utc = models.DateTimeField()
    score = models.IntegerField()
    domain = models.CharField(max_length=100)
    tid = models.CharField(max_length=30)
    title = models.TextField()
    author = models.CharField(max_length=50)
    ups = models.IntegerField()
    downs = models.IntegerField()
    num_comments = models.IntegerField()
    permalink = models.CharField(max_length=300)
    selftext = models.CharField(max_length=200)
    link_flair_text = models.CharField(max_length=300)
    over_18 = models.BooleanField()
    thumbnail = models.CharField(max_length=30)
    subreddit_id = models.CharField(max_length=50)
    edited = models.BooleanField()
    link_flair_css_class = models.CharField(max_length=30)
    author_flair_css_class = models.CharField(max_length=30)
    is_self = models.BooleanField()
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    distinguished = models.CharField(max_length=30)

