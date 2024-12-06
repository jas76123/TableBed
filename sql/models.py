from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship('User', back_populates='role')

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    fio = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    is_block = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role', back_populates='users')