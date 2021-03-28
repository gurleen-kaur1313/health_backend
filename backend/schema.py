import graphene
import graphql_jwt
import UserProfile.schema


class Query(UserProfile.schema.Query, graphene.ObjectType):
    pass


class Mutation(UserProfile.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)
