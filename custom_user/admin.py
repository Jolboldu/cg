from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Teacher, Accountant, Admin

# Register your models here.


class MyAdmin(UserAdmin):
    pass


admin.site.register(User, MyAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Accountant)
admin.site.register(Admin)

