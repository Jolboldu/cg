import graphene
from graphene_django import DjangoObjectType
from .models import Courses, Lessons, Files, Assignments, Attendance
from django.db.models import Q
from graphene_file_upload.scalars import Upload


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
    lessons = graphene.List(LessonType, lesson=graphene.Int())
    assignments = graphene.List(AssignmentType, course=graphene.Int(), lesson=graphene.Int(),
                                user=graphene.Int())
    attendance = graphene.List(AttendanceType, user=graphene.Int())

# query for courses
    def resolve_courses(self, info):
        return Courses.objects.all()

# query for files
    def resolve_files(self, info, user=None, is_material=None, course=None, lesson=None, file=None, **kwargs):
        # пока что хз как исправить is_material
        # if not is_material:
        #     filter=(
        #         Q(is_material__icontains=is_material)
        #     )
        #     return Files.objects.filter(filter)

        # if is_material:
        #     filter = (
        #         Q(is_material__icontains=is_material)
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
        if lesson:
            filter = (
                Q(lesson__id__icontains=lesson)
            )
            return Files.objects.filter(filter)
        if file:
            filter = (
                Q(id__icontains=file)
            )
            return Files.objects.filter(filter)


        return Files.objects.filter(filter)

# query for lessons
    def resolve_lessons(self, info, lesson=None, **kwargs):
        if lesson:
            filter = (
                Q(lesson__id__icontains=lesson)
            )
            return Lessons.objects.filter(filter)
        return Lessons.objects.all()

# query for assignments
    def resolve_assignments(self, info, user=None, course=None, lesson=None, **kwargs):
        if user:
            filter = (
                Q(user__id__icontains=user)
            )
            return Assignments.objects.filter(filter)

        if course:
            filter = (
                Q(course__id__icontains=course)
            )
            return Assignments.objects.filter(filter)
        if lesson:
            filter = (
                Q(lesson__id__icontains=lesson)
            )
            return Assignments.objects.filter(filter)

        return Assignments.objects.all()

# query for attendance
    def resolve_attendance(self, info, user=None, **kwargs):
        if user:
            filter = (
                Q(user__id__icontains=user)
            )
            return Attendance.objects.filter(filter)
        return Attendance.objects.all()


class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        # do something with your file

        return UploadMutation(success=True)