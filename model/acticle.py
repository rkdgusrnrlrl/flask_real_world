from extensions import db
from model.user import User
from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey, orm, func
from common.common import to_dict


class Article(db.Base):
    __tablename__ = 'articles'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    title  = Column(Text)
    body = Column(Text)
    slug = Column(Text)
    author = orm.relationship(User)
    author_uid = Column(Integer, ForeignKey('users.uid'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime)

    def __init__(self, title, author ,slug, body, discription):
        self.title = title
        self.body = body
        self.author = author
        self.slug = slug

    def to_dict(self):
        dict = to_dict(self, self.__class__)
        return dict