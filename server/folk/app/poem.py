
#!/usr/bin/env python3
# coding: utf-8
import time
from folk.db.model import Poem
from folk.db.base import session

class PoemLogic(object):

    @classmethod
    def create_single_poem(cls, title, content):
        new_poem = Poem()
        new_poem.title = title
        new_poem.content = content
        new_poem.time_created = time.time()
        session.add(new_poem)
        session.commit()
        return new_poem


    @classmethod
    def update_poem(cls, id, title, content):
        poem = query(Poem).filter(Poem.id == id).first()
        poem.title = title
        poem.content = content
        session.add(poem)
        session.commit()
        return poem
    
    @classmethod
    def get_poem_by_id(cls, id):
        return query(Poem).filter(Poem.id == id).first()
