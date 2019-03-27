import graphene
import graphql_jwt
import custom_user.schema
import education.schema
import encouragement.schema


class Query(custom_user.schema.Query, education.schema.Query, encouragement.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
