from django.db import models
from custom_user.models import Teacher, Student
# Create your models here.


class Teams(models.Model):
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()


class Participants(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
