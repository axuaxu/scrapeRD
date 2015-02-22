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
    created_utc = models.TextField(blank=True)
    score =  models.TextField(blank=True)
    domain =  models.TextField(blank=True)
    tid =  models.TextField(blank=True)
    title =  models.TextField(blank=True)
    author =  models.TextField(blank=True)
    ups =  models.TextField(blank=True)
    downs =  models.TextField(blank=True)
    num_comments = models.TextField(blank=True)
    permalink = models.TextField(blank=True)
    selftext =  models.TextField(blank=True)
    link_flair_text =  models.TextField(blank=True)
    over_18 = models.TextField(blank=True)
    thumbnail =  models.TextField(blank=True)
    subreddit_id =  models.TextField(blank=True)
    edited =  models.TextField(blank=True)
    link_flair_css_class =  models.TextField(blank=True)
    author_flair_css_class =  models.TextField(blank=True)
    is_self =  models.TextField(blank=True)
    name =  models.TextField(blank=True)
    url =  models.TextField(blank=True)
    distinguished =  models.TextField(blank=True)


class RedditSub(models.Model):
    """
      Reddit Sub categories CSV File
    """
    subcat = models.CharField(max_length=30)
    load = models.BooleanField()



