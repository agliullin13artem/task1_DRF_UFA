from django.contrib import admin
from groups.models import Stream, Group, Course
from django.contrib.auth.models import User



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (['id'])

