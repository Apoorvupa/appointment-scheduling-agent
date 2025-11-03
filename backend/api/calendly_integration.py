from fastapi import APIRouter
from datetime import datetime, timedelta
import json

router = APIRouter()

with open("data/doctor_schedule.json") as f:
    doctor_schedule = json.load(f)

@router.get("/api/calendly/availability")
def get_availability(date: str, appointment_type: str):
    slots = doctor_schedule.get(appointment_type, [])
    available_slots = []
    for s in slots:
        start_dt = datetime.strptime(s, "%H:%M")
        end_dt = (start_dt + timedelta(minutes=30)).strftime("%H:%M")
        available_slots.append({"start_time": s, "end_time": end_dt, "available": True})
    return {"date": date, "available_slots": available_slots}

@router.post("/api/calendly/book")
def book_appointment(appointment_type: str, date: str, start_time: str, patient: dict, reason: str):
    return {
        "booking_id": "APPT-2024-001",
        "status": "confirmed",
        "confirmation_code": "ABC123",
        "details": {
            "appointment_type": appointment_type,
            "date": date,
            "start_time": start_time,
            "patient": patient,
            "reason": reason
        }
    }
