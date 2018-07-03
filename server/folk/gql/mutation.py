#!/usr/bin/env python3
# coding: utf-8

import graphene
from folk.db.model import Poem
from folk.app.poem import PoemLogic
from folk.gql.query import PoemQuery


class CreatePoem(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    poem = graphene.Field(lambda: PoemQuery)

    @classmethod
    def _create_poem(cls, title, content):
        new_poem = PoemLogic.create_single_poem(title, content)
        return new_poem


    def mutate(self, info, title, content):
        new_poem = CreatePoem._create_poem(title, content)
        return CreatePoem(poem=new_poem)


class Mutation(graphene.ObjectType):
    create_poem = CreatePoem.Field()