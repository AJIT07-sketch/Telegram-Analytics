from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import SessionLocal, Group, Member, Message

def total_groups():
    db = SessionLocal()
    count = db.query(Group).count()
    db.close()
    return count

def group_type_distribution():
    db = SessionLocal()
    distribution = db.query(Group.group_type, func.count(Group.group_type)).group_by(Group.group_type).all()
    db.close()
    return {group_type: count for group_type, count in distribution}
