

from operator import length_hint
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Date, create_engine
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime
from wtf_models import Address_wtf 

engine = create_engine('sqlite:///market.db?check_same_thread=False')
DeclarativeBase = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    __abstract__ = True

    def __repr__(self) -> str:
        items = []
        for key in self.__table__._columns._data.keys():
            val = self.__getattribute__(key)
            items.append(f'{key}={val}')
        key_vals = ' '.join(items)
        name = self.__class__.__name__
        return f"<{name}({key_vals})>"

class User(Base, UserMixin):
    __tablename__= "Users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(84), nullable = False)
    date = db.Column(db.String(84), nullable = False)
    email = db.Column( db.String(82), nullable = False,  unique= True)
    cpf = db.Column( db.Integer, nullable = False, unique = True)
    phone = db.Column( db.Integer, nullable = False, unique = True)
    gender = db.Column( db.String(12), nullable = False, unique = False)
    password = db.Column( db.String(82), nullable = False)
    addresses = db.relationship('Address', backref='user', lazy=True)
    time = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    
class Address(Base, UserMixin):
    __tablename__= "Address"  
    id = db.Column(db.Integer, primary_key = True) 
    id_user = db.Column(db.Integer, db.ForeignKey('Users.id'))
    name = db.Column(db.String(84), nullable = False)
    cep = db.Column(db.Integer, nullable = False)
    street = db.Column(db.String(84), nullable = False)
    number = db.Column(db.Integer, nullable = False)
    complement = db.Column(db.String(84), nullable = False)
    zone = db.Column(db.String(32), nullable = False)
    city = db.Column(db.String(32), nullable = False)
    state = db.Column(db.String(32), nullable = False)
    time = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

    # def __str__(self):
    #     return self.name

class DefaultAddress(Base, UserMixin):
    __tablename__ = "DefaultAddress"
    id = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey('Users.id'), unique = True, nullable = False)
    id_address = db.Column(db.Integer, db.ForeignKey('Address.id'), unique = True, nullable = False)
    
    
class Cards(Base, UserMixin):
    __tablename__="Cards" 
    id = db.Column(db.Integer, primary_key = True) 
    id_user = db.Column(db.Integer, db.ForeignKey('Users.id'))     
    card_number = db.Column(db.Integer, nullable = False)
    name_card = db.Column(db.String(84), nullable = False)
    valid_date = db.Column(db.String(84), nullable = False)
    code = db.Column(db.Integer, nullable = False)
    

Base.metadata.create_all(engine)







   