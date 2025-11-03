from backend.rag.faq_rag import answer_faq
import requests

agent_state = {}

def process_message(user_id, message):
    state = agent_state.get(user_id, {"stage": "start"})
    
    if "insurance" in message.lower():
        return answer_faq(message)
    
    if state["stage"] == "start":
        agent_state[user_id] = {"stage": "ask_type"}
        return "Hi! What's the reason for your visit today?"
    
    if state["stage"] == "ask_type":
        agent_state[user_id]["appointment_type"] = "consultation"
        agent_state[user_id]["stage"] = "ask_date"
        return "Great. Which date do you prefer?"
    
    if state["stage"] == "ask_date":
        # call mock API
        resp = requests.get(f"http://localhost:8000/api/calendly/availability?date=2024-01-15&appointment_type=consultation")
        slots = resp.json()["available_slots"]
        slot_list = "\n".join([f"- {s['start_time']}" for s in slots])
        agent_state[user_id]["stage"] = "book_slot"
        return f"Here are available slots:\n{slot_list}\nWhich one works for you?"
    
    if state["stage"] == "book_slot":
        agent_state[user_id]["selected_slot"] = message
        agent_state[user_id]["stage"] = "collect_info"
        return "Please provide your name, email, and phone number for booking."
    
    if state["stage"] == "collect_info":
        # Very simple parsing
        name, email, phone = message.split(",")
        patient = {"name": name.strip(), "email": email.strip(), "phone": phone.strip()}
        slot = agent_state[user_id]["selected_slot"]
        resp = requests.post("http://localhost:8000/api/calendly/book",
                             json={"appointment_type": "consultation", "date": "2024-01-15",
                                   "start_time": slot, "patient": patient, "reason": "Checkup"})
        agent_state[user_id]["stage"] = "done"
        return f"Booking confirmed! {resp.json()['confirmation_code']}"
