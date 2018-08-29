
#!/usr/bin/env python3
# coding: utf-8
import time
from folk.db.model import Poem
from folk.db.base import session

class PoemLogic(object):

    @classmethod
    def create_single_poem(cls, name, content):
        new_poem = Poem()
        new_poem.name = name
        new_poem.content = content
        new_poem.time_created = time.time()
        session.add(new_poem)
        session.commit()
        return new_poem


    @classmethod
    def update_poem(cls, id, name, content):
        poem = session.query(Poem).filter(Poem.id == id).first()
        poem.name = name
        poem.content = content
        session.add(poem)
        session.commit()
        return poem


    @classmethod
    def get_poem_by_id(cls, id):
        return session.query(Poem).filter(Poem.id == id).first()


    @classmethod
    def get_poems(cls):
        return session.query(Poem)