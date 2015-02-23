from django.contrib import admin
from crawlRD.models import RedditPage,RedditCSV,RedditSub,RedditCSVcat
# Register your models here.
class RedditPageAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','rdTitle','rdVote','rdComments','rdLink','rdDateTime')

class RedditCSVAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','score','domain','tid','title','selftext','subreddit_id','num_comments','permalink')
    list_filter = ['subreddit_id']

class RedditSubAdmin(admin.ModelAdmin):
     list_display = ('id','subcat','load')

class RedditCSVcatAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','score','title','num_comments','url','created_utc','domain','catName')
    list_filter = ['catName']
    ordering = ('-score',)

admin.site.register(RedditPage,RedditPageAdmin)
admin.site.register(RedditCSV,RedditCSVAdmin)
admin.site.register(RedditSub,RedditSubAdmin)
admin.site.register(RedditCSVcat,RedditCSVcatAdmin)