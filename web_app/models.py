from flask_login import UserMixin
from sqlalchemy.sql import func
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
DB_NAME = "database.db"

def create_database():
    engine = create_engine(f"sqlite:///{DB_NAME}", echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class Admin(Base, UserMixin):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String(150), unique=True)
    password = db.Column("password", db.String(150))
    first_name = db.Column("first_name", db.String(150))
    session = create_database()
    def __init__(self,id,email,password,first_name):
        self.id= id
        self.email= email
        self.password= password
        self.first_name= first_name



class News(Base):
    __tablename__ = "news"
    __table_args__ = {'extend_existing': True}
    id = db.Column("id",db.Integer, primary_key=True)
    title = db.Column("title",db.String(200))
    content = db.Column("content",db.String(10000))
    image = db.Column("image",db.String(2000))
    session = create_database()

    def __init__(self,id,title,content,image):
        self.id=id
        self.title=title
        self.content=content
        self.image=image



