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
        

class Argia(Base):
    __tablename__ = 'argia'
    id = Column(Integer, primary_key=True)
    argia= Column(Float, nullable=False)
    ordua= Column(DateTime, nullable=False)

class Mugimendua(Base):
    __tablename__ = 'mugimendua'
    id = Column(Integer, primary_key=True)
    mugimendua= Column(Float, nullable=False)
    ordua= Column(DateTime, nullable=False)

class Ponpa(Base):
    __tablename__ = 'ponpa'
    id = Column(Integer, primary_key=True)
    ponpa= Column(Float, nullable=False)
    ordua= Column(DateTime, nullable=False)

class Konfigurazioa(Base):
    __tablename__ = 'konfigurazioa'
    giltza = Column(String, primary_key=True)
    balioa= Column(Float, nullable=False)
    



