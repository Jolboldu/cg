from django.db import models
# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=100, default="course")
    instructor = models.ForeignKey('custom_user.Teacher', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Lessons(models.Model):
    name = models.CharField(max_length=100, default="lesson")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    content = models.TextField()
    deadline = models.DateTimeField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Files(models.Model):
    name = models.CharField(max_length=100, default="file")
    date_time = models.DateTimeField()
    path = models.FileField(upload_to="media/")
    is_material = models.BooleanField(default=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    user = models.ForeignKey('custom_user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Assignments(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    user = models.ForeignKey('custom_user.Student', on_delete=models.CASCADE)
    instructor = models.ForeignKey('custom_user.Teacher', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    deadline = models.DateTimeField()
    description = models.TextField()
    comments = models.TextField()


class Attendance(models.Model):
    student = models.ForeignKey('custom_user.Student', on_delete=models.CASCADE)
    instructor = models.ForeignKey('custom_user.Teacher', on_delete=models.CASCADE)
    date = models.DateField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)

