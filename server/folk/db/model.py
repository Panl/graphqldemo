#!/usr/bin/env python3
# coding: utf-8

from sqlalchemy import Column, Integer, String, JSON
from folk.db.base import Base, engine

class Poem(Base):
    __tablename__ = 'Poem'

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    content = Column(String(256))
    author_id = Column(Integer)
    time_created = Column(Integer)
    time_removed = Column(Integer)


    def __repr__(self):
        return "<Poem(name='%s', content='%s')>" % (self.name, self.content)

Base.metadata.create_all(engine)
