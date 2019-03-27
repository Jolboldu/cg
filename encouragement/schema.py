import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Medal, Tree


class MedalType(DjangoObjectType):
    class Meta:
        model = Medal


class TreeType(DjangoObjectType):
    class Meta:
        model = Tree


class Query(graphene.ObjectType):
    medals = graphene.List(MedalType, user=graphene.Int())
    trees = graphene.List(TreeType, _from=graphene.Int(), _to=graphene.Int())

    def resolve_medals(self, info, user=None, description=None, **kwargs):
        if user:
            filter = (
                Q(user__user__id__icontains=user)
            )
            return Medal.objects.filter(filter)
        return Medal.objects.all()

    def resolve_trees(self, info, _from=None, _to=None, **kwargs):
        filter = (
            Q(_from__id__icontains=_from) |
            Q(_to__id__icontains=_to)
        )
        return Tree.objects.filter(filter)
