import graphene
from graphene_django import DjangoObjectType
from .models import Courses, Lessons, Files, Assignments, Attendance, Teams


class CourseType(DjangoObjectType):
    class Meta:
        model = Courses


class FileType(DjangoObjectType):
    class Meta:
        model = Files


class LessonType(DjangoObjectType):
    class Meta:
        model = Lessons


class AssignmentType(DjangoObjectType):
    class Meta:
        model = Assignments


class AttendanceType(DjangoObjectType):
    class Meta:
        model = Attendance


class TeamType(DjangoObjectType):
    class Meta:
        model = Teams


class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)
    files = graphene.List(FileType)
    lessons = graphene.List(LessonType)
    assignments = graphene.List(AssignmentType)
    attendance = graphene.List(AttendanceType)
    teams = graphene.List(TeamType)

    def resolve_courses(self, info):
        return Courses.objects.all()

    def resolve_files(self, info):
        return Files.objects.all()

    def resolve_lessons(self, info):
        return Lessons.objects.all()

    def resolve_assignments(self, info):
        return Assignments.objects.all()

    def resolve_attendance(self, info):
        return Attendance.objects.all()

    def resolve_teams(self, info):
        return Teams.objects.all()
