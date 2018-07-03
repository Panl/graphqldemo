#!/usr/bin/env python3
# coding: utf-8

from sqlalchemy import Column, Integer, String
from folk.db.base import Base

class Poem(Base):
    __tablename__ = 'Poem'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
    author_id = Column(Integer)
    time_created = Column(Integer)
    time_removed = Column(Integer)


    def __repr__(self):
        return "<Poem(name='%s', content='%s')>" % (self.name, self.content)
