from django.contrib import admin

from subs.models import Sub


@admin.register(Sub)
class SubAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'is_active',)
    list_filter = ('user',)
    search_fields = ('user',)
