from django.contrib import admin
from .models import Courses, Lessons, Files,Attendance,Assignments
# Register your models here.
admin.site.register(Courses)
admin.site.register(Lessons)
admin.site.register(Files)
admin.site.register(Assignments)
admin.site.register(Attendance)
