# backend/agent/scheduling_agent.py
import datetime

user_context = {}

def process_message(user_id, message):
    """
    Simple state-based conversational flow for appointment scheduling
    """

    # Get user context (previous state)
    state = user_context.get(user_id, {"step": "start"})

    msg = message.lower()

    # Step 1: Greeting
    if state["step"] == "start":
        user_context[user_id] = {"step": "ask_reason"}
        return "Hi! What's the reason for your visit today?"

    # Step 2: Ask appointment type
    elif state["step"] == "ask_reason":
        user_context[user_id] = {
            "step": "ask_date",
            "reason": message,
        }
        return "Got it. What type of appointment would you like (e.g., General consultation, Dental, etc.)?"

    # Step 3: Ask date
    elif state["step"] == "ask_date":
        user_context[user_id]["appointment_type"] = message
        user_context[user_id]["step"] = "ask_time"
        return "Great. Which date would you prefer?"

    # Step 4: Ask time
    elif state["step"] == "ask_time":
        user_context[user_id]["date"] = message
        user_context[user_id]["step"] = "ask_contact"
        return "Perfect. What time would you like?"

    # Step 5: Ask patient details
    elif state["step"] == "ask_contact":
        user_context[user_id]["time"] = message
        user_context[user_id]["step"] = "confirm_details"
        return "Please share your details: name, email, and phone number."

    # Step 6: Confirmation
    elif state["step"] == "confirm_details":
        user_context[user_id]["details"] = message
        user_context[user_id]["step"] = "completed"

        booking_info = user_context[user_id]
        return (
            f"✅ Booking confirmed!\n\n"
            f"**Appointment Type:** {booking_info['appointment_type']}\n"
            f"**Date:** {booking_info['date']}\n"
            f"**Time:** {booking_info['time']}\n"
            f"**Reason:** {booking_info['reason']}\n"
            f"**Patient Info:** {booking_info['details']}\n\n"
            f"Confirmation ID: APPT-{datetime.datetime.now().strftime('%Y%m%d%H%M')}"
        )

    # Default fallback
    else:
        return "I'm not sure I understood that. Could you please repeat?"
