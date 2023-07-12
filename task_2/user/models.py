from sqlalchemy import Column, Integer, String

from settings.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String)
    password = Column(String(length=1024), nullable=False)

