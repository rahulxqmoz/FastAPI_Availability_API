from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    timezone = Column(String)

    availabilities = relationship("Availability", back_populates="user")

class Availability(Base):
    __tablename__ = 'availabilities'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    is_specific = Column(Integer, default=0)  # 0 for weekly, 1 for specific date

    user = relationship("User", back_populates="availabilities")

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)

