from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Database:

    def __init__(self):
        self.engine = None

        self.Base = declarative_base()
        self.session = scoped_session(sessionmaker(bind=self.engine))

    def init_app(self, app):
        # lazy init
        url = app.config["SQLALCHEMY_DATABASE_URI"]
        self.init_engine(config=app.config)

        @app.teardown_appcontext
        def teardown_db(resp_or_exc):
            self.session.remove()
            return resp_or_exc

    def init_engine(self, config):
        self.session.remove()

        if not hasattr(config, "SQLALCHEMY_DATABASE_URI"): # flask config instance
            self.engine = create_engine(config["SQLALCHEMY_DATABASE_URI"])
        elif config.SQLALCHEMY_DATABASE_URI is not None : # config instance
            self.engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        else:
            self.engine = create_engine()

        self.session = scoped_session(sessionmaker(bind=self.engine))

    def init_model(self):
        if self.engine is None:
            raise Exception("engine is not init")

        self.Base.metadata.create_all(self.engine)
