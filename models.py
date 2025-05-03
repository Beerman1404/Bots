from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///users.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True)

Base.metadata.create_all(bind=engine)