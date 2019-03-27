import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Teams,Participants


class TeamType(DjangoObjectType):
    class Meta:
        model = Teams


class ParticipantType(DjangoObjectType):
    class Meta:
        model = Participants


class Query(graphene.ObjectType):
    teams = graphene.List(TeamType, instructor=graphene.Int())
    participants = graphene.List(ParticipantType, id=graphene.Int())

    def resolve_teams(self, info, instructor=None, **kwargs):
        if instructor:
            filter = (
                Q(instructor__user__id__icontains=instructor)
            )
            return Teams.objects.filter(filter)
        return Teams.objects.all()
