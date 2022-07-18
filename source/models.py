from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from source.database import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_chat.id"))
    title = Column(String)
    current_page = Column(Integer, default=True)
    total_pages = Column(Integer, default=True)

class UserChat(Base):
    __tablename__ = "user_chat"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    creation_ts = Column(String, )

    owner = relationship("Book", back_populates="items")
