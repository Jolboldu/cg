import graphene
from graphene_django import DjangoObjectType
from .models import Courses, Lessons, Files, Assignments, Attendance
from django.db.models import Q


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


class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)
    files = graphene.List(FileType, user=graphene.Int(), is_material=graphene.Boolean(),
                          course=graphene.Int(), lesson=graphene.Int(), file=graphene.Int())
    lessons = graphene.List(LessonType)
    assignments = graphene.List(AssignmentType)
    attendance = graphene.List(AttendanceType)

    def resolve_courses(self, info):
        return Courses.objects.all()

    def resolve_files(self, info, user=None, is_material=bool, course=None, lesson=int, file=None, **kwargs):
        #пока что хз как исправить is_material
        # if not is_material:
        #     filter=(
        #         Q(is_material__icontains=is_material)
        #     )
        #     return Files.objects.filter(filter)

        # if is_material:
        #     filter = (
        #         Q(is_material__icontains=not is_material)
        #     )
        #     return Files.objects.filter(filter)

        if user:
            filter = (
                Q(user__id__icontains=user)
            )
            return Files.objects.filter(filter)

        if course:
            filter = (
                Q(course__id__icontains=course)
            )
            return Files.objects.filter(filter)
        if file:
            filter = (
                Q(id__icontains=file)
            )
            return Files.objects.filter(filter)

        return Files.objects.all()

    def resolve_lessons(self, info):
        return Lessons.objects.all()

    def resolve_assignments(self, info):
        return Assignments.objects.all()

    def resolve_attendance(self, info):
        return Attendance.objects.all()

