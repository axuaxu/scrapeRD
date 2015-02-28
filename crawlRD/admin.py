from django.contrib import admin
from crawlRD.models import RedditPage,RedditCSV,RedditSub,RedditCSVcat,RedditPedia,Reddit
# Register your models here.
#loadCSVsubCatDate.py    load table  crawlRD_redditcsvcat   load the reddit csv files
#updCSVload.py           update set table crawlRD_redditsub  csv file list
#updCSVloadClear.py      clear setting in table  crawlRD_redditsub

#----
#loadCSVReddit.py    load table  crawlRD_reddit 'en.wikipeida.org'   load the reddit csv files
#
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
     search_fields = ['subcat']

class RedditCSVcatAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','tid','score','title','num_comments','url','created_utc','domain','catName')
    list_filter = ['catName','domain']
    ordering = ('-score',)

class RedditPediaAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','tid','score','title','num_comments','url','created_utc','domain','catName')
    list_filter = ['catName','domain']
    ordering = ('-score',)

class RedditAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','tid','score','title','num_comments','url','created_utc','domain','catName')
    list_filter = ['catName','domain']
    ordering = ('-score',)

admin.site.register(RedditPage,RedditPageAdmin)
admin.site.register(RedditCSV,RedditCSVAdmin)
admin.site.register(RedditSub,RedditSubAdmin)
admin.site.register(RedditCSVcat,RedditCSVcatAdmin)
admin.site.register(RedditPedia,RedditPediaAdmin)
admin.site.register(Reddit,RedditAdmin)