import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from .models import UserProfile
from graphql import GraphQLError
from django.db.models import Q


class Profile(DjangoObjectType):
    class Meta:
        model = UserProfile


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    me = graphene.Field(Profile)
    leader_board = graphene.List(Profile)

    def resolve_leader_board(self, info, **kwargs):
        u = info.context.user
        if u.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return UserProfile.objects.all().order_by("-max_score")

    def resolve_me(self, info):
        u = info.context.user
        if u.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return UserProfile.objects.get(user=u)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        name = graphene.String()
        gender = graphene.String()
        age = graphene.Int()
        weight = graphene.Int()
        height = graphene.Int()

    def mutate(self, info, username, password, email, **kwargs):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        profile = UserProfile.objects.create(user=user, name=kwargs.get(
            "name"),  gender=kwargs.get("gender"), age=kwargs.get("age"), height=kwargs.get("height"), weight=kwargs.get("weight"))
        profile.bmi = kwargs.get("weight")*100*100/pow(kwargs.get("height"), 2)
        profile.save()

        return CreateUser(user=user)


class UpdateScore(graphene.Mutation):
    update = graphene.Field(Profile)

    class Arguments:
        life = graphene.Int(required=False)
        score = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        profile = UserProfile.objects.get(user=user)

        score = kwargs.get("name")
        lifes = kwargs.get("image")

        profile.max_score = score
        profile.game_life = lifes
        profile.save()

        return UpdateScore(update=profile)


class DeleteUser(graphene.Mutation):
    user = graphene.String()

    def mutate(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        user.delete()
        str = "Done!"

        return DeleteUser(user=str)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateScore.Field()
    delete_user = DeleteUser.Field()
