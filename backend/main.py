from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Shopease API",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": os.getenv("APP_ENV")
    }
