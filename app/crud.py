  
from sqlalchemy.orm import Session
from app import models,schemas

def get_users_by_ids(db: Session, user_ids: list[int]):
    return db.query(models.User).filter(models.User.id.in_(user_ids)).all()

def get_availabilities_for_users(db: Session, user_ids: list[int], start_date, end_date):
    return db.query(models.Availability).filter(
        models.Availability.user_id.in_(user_ids),
        models.Availability.date.between(start_date, end_date)
    ).all()

def get_events_for_users(db: Session, user_ids: list[int], start_date, end_date):
    return db.query(models.Event).filter(
        models.Event.user_id.in_(user_ids),
        models.Event.date.between(start_date, end_date)
    ).all()

def create_availability(db: Session, availability: schemas.AvailabilityCreate):
    db_availability = models.Availability(**availability.dict())
    db.add(db_availability)
    db.commit()
    db.refresh(db_availability)
    return db_availability


def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def delete_availability(db: Session, availability_id: int):
    db_availability = db.query(models.Availability).filter(models.Availability.id == availability_id).first()
    if db_availability:
        db.delete(db_availability)
        db.commit()
    return db_availability


def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event
