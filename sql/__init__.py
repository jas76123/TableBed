from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Role

# Создаем подключение к базе данных
engine = create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker(bind=engine)

def create_db():
    Base.metadata.create_all(engine)

__all__ = ['User', 'Role', 'create_db', 'Session']