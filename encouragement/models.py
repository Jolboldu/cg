from django.db import models
from custom_user.models import Student
# Create your models here.


class Medal(models.Model):
    medal = models.CharField(max_length=100, default="medal")
    description = models.TextField()
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_time = models.DateTimeField()


class Tree(models.Model):
    _from = models.ForeignKey(Medal, related_name='medal_from', on_delete=models.CASCADE)
    _to = models.ForeignKey(Medal, related_name='medal_to', on_delete=models.CASCADE)
