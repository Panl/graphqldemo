#!/usr/bin/env python3
# coding: utf-8

import graphene
from folk.db.model import Poem
from folk.app.poem import PoemLogic
from folk.gql.query import PoemQuery


class CreatePoem(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        content = graphene.String()

    poem = graphene.Field(lambda: PoemQuery)

    @classmethod
    def _create_poem(cls, name, content):
        new_poem = PoemLogic.create_single_poem(name, content)
        return new_poem


    def mutate(self, info, name, content):
        new_poem = CreatePoem._create_poem(name, content)
        return CreatePoem(poem=new_poem)

class UpdatePoem(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        content =graphene.String()

    poem = graphene.Field(lambda: PoemQuery)

    @classmethod
    def _update_poem(cls, id, name, content):
        new_poem = PoemLogic.update_poem(id, name, content)
        return new_poem
    
    def mutate(self, info, id, name, content):
        new_poem = UpdatePoem._update_poem(id, name, content)
        return CreatePoem(poem=new_poem)


class Mutation(graphene.ObjectType):
    create_poem = CreatePoem.Field()
    update_poem = UpdatePoem.Field()