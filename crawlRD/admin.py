from django.contrib import admin
from crawlRD.models import RedditPage
# Register your models here.
class RedditPageAdmin(admin.ModelAdmin):
    # ...
    #list_display = ('id','rdTitle','rdVote','rdComments','rdDomain','rdFullName','rdDateTime', 'rdSubmitter')
    list_display = ('id','rdTitle','rdVote','rdComments','rdDateTime')

admin.site.register(RedditPage,RedditPageAdmin)