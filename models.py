from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config import engine

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Group(Base):
    __tablename__ = "groups"
    group_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    group_type = Column(String, nullable=False)
    member_count = Column(Integer)
    admin_count = Column(Integer)
    number_of_bots = Column(Integer)
    pinned_messages = Column(String, nullable=True)
    pinned_messages_timestamp = Column(TIMESTAMP, nullable=True)
    visibility = Column(String, nullable=True)

class Member(Base):
    __tablename__ = "members"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_bot = Column(Boolean, nullable=False, default=False)
    role = Column(String, nullable=False)
    join_date = Column(TIMESTAMP, nullable=True)
    group_id = Column(Integer, ForeignKey("groups.group_id"))

class Message(Base):
    __tablename__ = "messages"
    message_id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("members.user_id"))
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    timestamp = Column(TIMESTAMP, nullable=False)
    message_type = Column(String, nullable=True)
    text = Column(String, nullable=True)
    media_links = Column(JSON, nullable=True)
    hashtags = Column(JSON, nullable=True)
    urls = Column(JSON, nullable=True)
    replies = Column(Integer, nullable=True)
    views = Column(Integer, nullable=True)
    forwards = Column(Integer, nullable=True)

Base.metadata.create_all(bind=engine)
