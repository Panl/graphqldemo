#!/usr/bin/env python3
# coding: utf-8

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from folk.db.model import Poem
from folk.app.poem import PoemLogic

class PoemQuery(SQLAlchemyObjectType):
    class Meta:
        model = Poem



class Query(graphene.ObjectType):
    
    poem = graphene.Field(PoemQuery, id=graphene.Int())

    # feed = graphene.Field(PoemFeed)

    poem_list = graphene.List(PoemQuery)
    
    def resolve_poem(self, info, id):
        print('pl---', id)
        return PoemLogic.get_poem_by_id(id)

    # def resolve_feed(self, info):
    #     return PoemFeed()

    def resolve_poem_list(self, info):
        return PoemLogic.get_poems()
