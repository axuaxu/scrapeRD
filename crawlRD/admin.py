from django.contrib import admin
from crawlRD.models import RedditPage
# Register your models here.
class RedditPageAdmin(admin.ModelAdmin):
    # ...
    list_display = ('id','rdTitle', 'rdDomain', 'rdSubmitter','rdLiFirst','rdFullName','rdDateTime')

admin.site.register(RedditPage,RedditPageAdmin)