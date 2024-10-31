from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from app.db.config import DB_URL


engine = create_engine(DB_URL)
session_maker = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


