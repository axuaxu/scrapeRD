from django.db import models

# Create your models here.

class RedditPage(models.Model):
    """
      Reddit Page Fields
    """
    rdTitle = models.TextField()
    rdDomain = models.CharField(max_length=200)
    rdSubmitter = models.CharField(max_length=300)
    rdVote = models.IntegerField()
    rdComments = models.IntegerField()
    rdFullName = models.CharField(max_length=50)
    rdDateTime = models.DateTimeField()




