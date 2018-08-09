from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    password = Column(String(50))
    token = Column(String(50))
    name = Column(String(50))
    bio = Column(Text)
    image = Column(String(50))

    def __init__(self, email, password, token, name, bio, image):
        self.email = email
        self.password = password
        self.token = token
        self.name = name
        self.bio = bio
        self.image = image