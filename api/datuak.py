#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String,Float,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
 
class Tenperatura(Base):
    __tablename__ = 'tenperatura'
    id = Column(Integer, primary_key=True)
    tenperatura= Column(Float, nullable=False)
    ordua= Column(DateTime, nullable=False)
        



