from common.common import ecrypto_password, to_dict

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    password = Column(String(50))
    token = Column(String(50))
    username = Column(String(50))
    bio = Column(Text)
    image = Column(String(50))

    def __init__(self, email, password, username, token=None, bio=None, image=None):
        self.email = email
        self.password =  ecrypto_password(password)
        self.token = token
        self.username = username
        self.bio = bio
        self.image = image

    def to_dict(self):
        dict = to_dict(self, self.__class__)
        del dict["password"]
        return dict
