from django.contrib import admin

from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', )  # 'owner'
    list_filter = ('title',)
    search_fields = ('title',)
