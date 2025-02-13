from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, utils
from app.database import SessionLocal
from typing import List, Dict

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/common-availability/", response_model=Dict[str, List[str]])
def get_common_availability(request: schemas.AvailabilityRequest, db: Session = Depends(get_db)):
    users = crud.get_users_by_ids(db, request.user_ids)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")

    availabilities = crud.get_availabilities_for_users(db, request.user_ids, request.start_date, request.end_date)
    events = crud.get_events_for_users(db, request.user_ids, request.start_date, request.end_date)

    common_slots = utils.find_common_slots(availabilities, events, request.timezone)
    return common_slots
