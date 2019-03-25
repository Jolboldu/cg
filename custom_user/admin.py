from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User, Student, Teacher, Accountant, Admin

# Register your models here.


# class MyUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User
#

class MyAdmin(UserAdmin):
    # form = MyUserChangeForm
    #
    # fieldsets = UserAdmin.fieldsets + (
    #         (None, {'fields': ('USER_TYPE_CHOICES',)}),
    # )
    pass


admin.site.register(User, MyAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Accountant)
admin.site.register(Admin)
