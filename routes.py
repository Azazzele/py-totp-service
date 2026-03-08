from fastapi import APIRouter
from security import HOTPGenerator, verify_totp

router = APIRouter()  

# Генерация TOTP по секрету
@router.get("/generate")
def generate(secret: str):
    otp_gen = HOTPGenerator(secret)
    return {"otp": otp_gen.generate_totp()}

# Генерация TOTP по секрету
@router.get("/verify")
def verify(secret: str, code: str):
    is_valid = verify_totp(secret, code)
    return {"valid": is_valid}

