
from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered Travel Recommendation Engine",
    description="Personalized travel and hotel recommendation system",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Travel Recommendation Engine",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Travel Recommendation API"
    }
