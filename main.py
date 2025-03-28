from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import re
from passlib.context import CryptContext

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordRequest(BaseModel):
    password: str

COMMON_PASSWORDS = {"password", "123456", "admin", "qwerty", "letmein", "welcome", "monkey", "football"}

def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak - Too short (min 8 characters required)"
    if not re.search(r"\d", password):
        return "Weak - Include at least one number"
    if not re.search(r"[A-Z]", password):
        return "Weak - Include at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak - Include at least one lowercase letter"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Improved special character check
        return "Medium - Consider adding special characters"
    if password.lower() in COMMON_PASSWORDS:
        return "Weak - Avoid common passwords"
    return "Strong - Good to go!"

@app.get("/")
def home():
    return {"message": "VaultCheck API is running!"}

@app.post("/check_password/")
def check_password(data: PasswordRequest, hash: bool = Query(default=False)):
    if not data.password:
        raise HTTPException(status_code=400, detail="Password cannot be empty")
    
    strength = check_password_strength(data.password)
    
    if hash:
        hashed_password = pwd_context.hash(data.password)
        return {"password": data.password, "strength": strength, "hashed": hashed_password}
    
    return {"password": data.password, "strength": strength}
