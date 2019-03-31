from .models import User, Student

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    students = graphene.List(StudentType)
    me = graphene.List(UserType)
    viewer = graphene.Field(UserType)
    def resolve_users(self, info):
        return User.objects.all()

    def resolve_students(self, info):
        return Student.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

    def resolve_viewer(self, info, **kwargs):
        print(info)
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        return user
