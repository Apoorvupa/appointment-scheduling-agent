from fastapi import FastAPI
from backend.api import calendly_integration

app = FastAPI()
app.include_router(calendly_integration.router)

@app.get("/")
def home():
    return {"message": "Medical Appointment Scheduling Agent is running!"}
