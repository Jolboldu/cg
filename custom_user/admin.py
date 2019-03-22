from django.contrib import admin
from .models import User, Student, Teacher, Accountant, Admin

# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Accountant)
admin.site.register(Admin)