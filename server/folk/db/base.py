#!/usr/bin/env python3
# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from folk.conf import database_url
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine(database_url, echo=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()
