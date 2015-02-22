from django.contrib import admin
from crawlRD.models import RedditPage,RedditCSV,RedditSub
# Register your models here.
class RedditPageAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','rdTitle','rdVote','rdComments','rdLink','rdDateTime')

class RedditCSVAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','created_utc','score','domain','tid','title','author','ups','downs','num_comments','permalink')

class RedditSubAdmin(admin.ModelAdmin):
     list_display = ('id','subcat','load')


admin.site.register(RedditPage,RedditPageAdmin)
admin.site.register(RedditCSV,RedditCSVAdmin)
admin.site.register(RedditSub,RedditSubAdmin)