from django.contrib import admin
from .models import *

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "source"]
    list_filter = ["author"]
    search_fields = ["author", "title"]
   
admin.site.register(News, NewsAdmin)

admin.site.register(Movies)


class Meta:
    verbose_name_plural = "News"