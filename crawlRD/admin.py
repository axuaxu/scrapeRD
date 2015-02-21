from django.contrib import admin
from crawlRD.models import RedditPage,RedditCSV
# Register your models here.
class RedditPageAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','rdTitle','rdVote','rdComments','rdLink','rdDateTime')

class RedditCSVAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('created_utc','score,domain','tid','title','author','ups','downs','num_comments','permalink')

admin.site.register(RedditPage,RedditPageAdmin)
admin.site.register(RedditCSV,RedditCSVAdmin)