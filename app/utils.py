from datetime import datetime, timedelta, time as dt_time
from pytz import timezone as tz
from sqlalchemy.orm import Session
from app import models, schemas

def convert_to_timezone(time, from_tz, to_tz):
    from_zone = tz(from_tz)
    to_zone = tz(to_tz)
    local_time = from_zone.localize(time)
    return local_time.astimezone(to_zone)

def is_time_conflict(slot_start, slot_end, event_start, event_end):
    return not (slot_end <= event_start or slot_start >= event_end)

def get_time_slots(start_time, end_time, interval_minutes=30):
    slots = []
    current_time = start_time
    while current_time < end_time:
        slot_end = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=interval_minutes)).time()
        if slot_end <= end_time:
            slots.append((current_time, slot_end))
        current_time = slot_end
    return slots

def get_availabilities_for_users(db: Session, user_ids: list[int], start_date, end_date):
    availabilities = db.query(models.Availability).filter(
        models.Availability.user_id.in_(user_ids),
        models.Availability.date.between(start_date, end_date)
    ).all()
    return availabilities

def get_events_for_users(db: Session, user_ids: list[int], start_date, end_date):
    events = db.query(models.Event).filter(
        models.Event.user_id.in_(user_ids),
        models.Event.date.between(start_date, end_date)
    ).all()
    return events

def find_common_slots(availabilities, events, timezone):
    availabilities_by_date = {}
    for availability in availabilities:
        date = availability.date
        if date not in availabilities_by_date:
            availabilities_by_date[date] = []
        availabilities_by_date[date].append(availability)

    common_slots = {}
    for date, daily_availabilities in availabilities_by_date.items():
        all_user_slots = []
        for availability in daily_availabilities:
            slots = get_time_slots(availability.start_time, availability.end_time)
            all_user_slots.append(slots)
        common = set(all_user_slots[0]).intersection(*all_user_slots[1:])
        for event in (events[date] if date in events else []):
            common = [slot for slot in common if not is_time_conflict(slot[0], slot[1], event.start_time, event.end_time)]
        common_slots[str(date)] = [f"{slot[0].strftime('%I:%M%p')} - {slot[1].strftime('%I:%M%p')}" for slot in common]

    return common_slots
