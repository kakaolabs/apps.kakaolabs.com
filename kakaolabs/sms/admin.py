from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms

from kakaolabs.sms import models


class CategoryAdmin(admin.ModelAdmin):
    raw_id_fields = ('parent', )
    list_display = ('name', 'type', 'parent', 'index')
    search_fields = ('name', )
    list_filter = ('type', )


class SMSContentAdmin(admin.ModelAdmin):
    raw_id_fields = ('category', )
    list_display = ('category', 'content', 'index', 'votes')
    list_filter = ('category', )


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.SMSContent, SMSContentAdmin)

