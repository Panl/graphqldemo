#!/usr/bin/env python3
# coding: utf-8

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from folk.db.model import Poem
from folk.app.poem import PoemLogic

class PoemQuery(SQLAlchemyObjectType):
    class Meta:
        model = Poem


class Query(graphene.ObjectType):

    hello = graphene.String()
    
    poem = graphene.Field(PoemQuery, id=graphene.ID())

    def resolve_hello(self, info):
        return 'Hello Graphql!'
    
    def resolve_poems(self, info, id):
        return PoemLogic.get_poem_by_id(id)
