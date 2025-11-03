from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from backend.api import calendly_integration , chat

app = FastAPI()

# Agar frontend React use kar raha hai (localhost:3000), to ye CORS fix karega
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(calendly_integration.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "Medical Appointment Scheduling Agent is running!"}
