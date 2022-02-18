from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings


Base = declarative_base()


def init_db():
    db_user = settings.DATABASE_USERNAME
    db_pass = settings.DATABASE_PASSWORD
    db_host = settings.DATABASE_HOST
    db_name = settings.DATABASE_NAME

    sqlalchemy_url = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"
    engine = create_engine(sqlalchemy_url)
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = DBSession()

    try:
        yield db
    finally:
        db.close()
