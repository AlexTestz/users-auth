# src/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import users_routes

app = FastAPI(
    title="Change Password Microservice",
    description="Microservice to allow users to change their password securely",
    version="1.0.0"
)

# CORS Middleware (si usas frontend como React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(users_routes.router)

# test
@app.get("/")
def root():
    return {"message": "✅ Change Password Service is running!"}
