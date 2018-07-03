#!/usr/bin/env python3
# coding: utf-8
import graphene
from folk.gql.query import Query
from folk.gql.mutation import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
