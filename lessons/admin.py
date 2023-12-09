from django.contrib import admin

from lessons.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', )  # 'owner'
    list_filter = ('title',)
    search_fields = ('title',)
