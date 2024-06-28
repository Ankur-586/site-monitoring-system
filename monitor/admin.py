from django.contrib import admin
from monitor.models import *

@admin.register(Site)
class siteAdmin(admin.ModelAdmin):
    list_display = ['website_name','website_url','created_at','updated_at']


@admin.register(Check)
class checkAdmin(admin.ModelAdmin):
    list_display = ['site','checked_at','status_code','response_time','created_at','updated_at']