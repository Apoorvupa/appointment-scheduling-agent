
from backend.agent.scheduling_agent import process_message


def test_booking_flow():
    user_id = "test_user"

    # Step 1: Start conversation
    response = process_message(user_id, "Hi, I need to see a doctor")
    print(response)

    # Step 2: Appointment type
    response = process_message(user_id, "General consultation")
    print(response)

    # Step 3: Preferred date
    response = process_message(user_id, "2024-01-15")
    print(response)

    # Step 4: Choose a time slot
    response = process_message(user_id, "09:00")
    print(response)

    # Step 5: Provide patient info
    response = process_message(user_id, "John Doe, john@example.com, +1-555-0100")
    print(response)








def test_no_slots():
    user_id = "no_slots_user"

    # Start conversation
    response = process_message(user_id, "Hi, I need a doctor")
    print(response)

    # Appointment type
    response = process_message(user_id, "Consultation")
    print(response)

    # Date with no slots (assume doctor_schedule me ye date empty hai)
    response = process_message(user_id, "2024-01-01")
    print(response)




def test_faq_mid_booking():
    user_id = "faq_user"

    # Start conversation
    response = process_message(user_id, "Hi")
    print(response)

    # Ask FAQ
    response = process_message(user_id, "What insurance do you accept?")
    print(response)

    # Continue booking
    response = process_message(user_id, "General consultation")
    print(response)



def test_invalid_input():
    user_id = "invalid_user"

    # Wrong appointment type
    response = process_message(user_id, "Ultra consultation")
    print(response)

    # Past date
    response = process_message(user_id, "2023-01-01")
    print(response)

