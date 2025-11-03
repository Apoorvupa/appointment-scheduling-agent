from fastapi import APIRouter, Request, HTTPException
from backend.agent.scheduling_agent import process_message

router = APIRouter(
    prefix="/api",
    tags=["Chat Agent"],
)

@router.post("/chat")
async def chat_endpoint(request: Request):
    try:
        data = await request.json()
        user_id = data.get("user_id", "guest")
        message = data.get("message", "").strip()

        if not message:
            raise HTTPException(status_code=400, detail="Message cannot be empty.")

        print(f"User({user_id}): {message}")  

        response = process_message(user_id, message)

        if not isinstance(response, str):
            response = str(response)

        print(f"Bot({user_id}): {response}")  

        return {"reply": response}

    except Exception as e:
        print(" Error in chat endpoint:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
