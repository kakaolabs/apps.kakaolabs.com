from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms

from kakaolabs.core import models


class AppAdmin(admin.ModelAdmin):
    raw_id_fields = ('member', 'devices')
    list_display = ('member', 'name', 'description')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_admin')
    list_filter = ('is_admin',)
    search_fields = ('email',)
    ordering = ('date_joined',)


admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.App, AppAdmin)
admin.site.register(models.AppVersion)
admin.site.register(models.Device)
