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

class PoemsConnection(relay.Connection):
    total_count = graphene.Int()
    page_info = graphene.PageInfo()
    next_offset = graphene.Int()

    class Meta:
        node = PoemQuery 

class PoemFeed(graphene.ObjectType):
    poems = relay.ConnectionField(PoemsConnection, offset=graphene.Int())


class Query(graphene.ObjectType):

    hello = graphene.String()
    
    poem = graphene.Field(PoemQuery, id=graphene.ID())

    feed = graphene.Field(PoemFeed)

    def resolve_hello(self, info):
        return 'Hello Graphql!'
    
    def resolve_poem(self, info, id):
        print('pl---', id)
        return PoemLogic.get_poem_by_id(id)

    def resolve_feed(self, info):
        return PoemFeed()
