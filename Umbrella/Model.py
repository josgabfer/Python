import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import platform
from os import path as dir

Base = declarative_base()
engine = create_engine('sqlite:///ConnectionSettings.db',echo=True)

class connectionSettingsModel(Base):
    __tablename__ = 'UmbrellaAPISettings'
    id = Column('ID', Integer, primary_key=True)
    name = Column('name',String,nullable=False,unique=True)
    orgid = Column('orgid', String,nullable=False,unique=True)
    key = Column('accesskey',String,nullable=False,unique=True)
    secret = Column('secret',String,nullable=False,unique=True)
    token = Column('token',String,nullable=False,unique=True)

def createTable(engine):
    meta = MetaData()
    APIConnectionSettings = Table(
        'UmbrellaAPISettings',meta,
        Column('ID',Integer,primary_key=True,autoincrement=True),
        Column('name',String,nullable=False,unique=True),
        Column('orgid', String,nullable=False,unique=False),
        Column('accesskey',String,nullable=False,unique=False),
        Column('secret',String,nullable=False,unique=False),
        Column('token',String,nullable=False,unique=True)
    )
    meta.create_all(engine)
    return 'Table succesfully created'


def saveConnectionSettings(APISettings):
    """Creates a connection to the SQLIte database, db_file is the db where this information is stored.
    Requires: APISettings obj, this function will create a DB on the same dir where the program is
    Returns a connection object or none"""
    engine = create_engine('sqlite:///ConnectionSettings.db',echo=True)
    if not engine.dialect.has_table(engine, 'UmbrellaAPISettings'):
        meta = MetaData()
        APIConnectionSettings = Table(
        'UmbrellaAPISettings',meta,
        Column('ID',Integer,primary_key=True,autoincrement=True),
        Column('name',String,nullable=False,unique=True),
        Column('orgid', String,nullable=False,unique=False),
        Column('accesskey',String,nullable=False,unique=False),
        Column('secret',String,nullable=False,unique=False),
        Column('token',String,nullable=False,unique=True)
        )
        meta.create_all(engine)
    connectionSettings = connectionSettingsModel()
    connectionSettings.name = APISettings.name
    connectionSettings.orgid = APISettings.orgid
    connectionSettings.key = APISettings.key
    connectionSettings.secret = APISettings.secret
    connectionSettings.token = APISettings.token


    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(connectionSettings)
        session.commit()
    except ConnectionError as e:
        print("Connection to the database was unsuccuesful:\n" + e)
    finally:
        session.close()



def saveConnectionSettingsPath(APISettings, path):
    """Creates a connection to the SQLIte database, db_file is the db where this information is stored.
    Requires: APISettings obj, and the path where the DB has to be saved, use -p or --path for this function
    Returns a connection object or none"""
    engine = create_engine('sqlite:///'+ path +'ConnectionSettings.db')
    connection = engine.connect()
    table = 'UmbrellaAPISettings'

    if not engine.dialect.has_table(engine, 'UmbrellaAPISettings'):
        meta = MetaData(engine)
        APIConnectionSettings = Table(
        'UmbrellaAPISettings',meta,
        Column('ID',Integer,primary_key=True,autoincrement=True),
        Column('name',String,nullable=False,unique=True),
        Column('orgid', String,nullable=False,unique=False),
        Column('accesskey',String,nullable=False,unique=False),
        Column('secret',String,nullable=False,unique=False),
        Column('token',String,nullable=False,unique=True)
        )
        meta.create_all(engine)

    print(engine)
    connectionSettings = connectionSettingsModel()
    connectionSettings.name = APISettings.name
    connectionSettings.orgid = APISettings.orgid
    connectionSettings.key = APISettings.key
    connectionSettings.secret = APISettings.secret
    connectionSettings.token = APISettings.token

    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(connectionSettings)
        session.commit()
    except ConnectionError as e:
        print("Connection to the database was unsuccuesful:\n" + e)
    finally:
        session.close()

def openConnectionSettings():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        readSettings = session.query(connectionSettingsModel).all()
        for setting in readSettings:
            print(setting)
    except ConnectionError as e:
        print("Connection to the database was unsuccuesful:\n" + e)
    finally:
        session.close()







