from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.services.firebase_auth import verify_firebase_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def current_user(token: str = Depends(oauth2_scheme)):
    user = verify_firebase_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    return user


@router.post("/verify")
def verify_token(token: str):
    user = verify_firebase_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unable to verify token")
    return {"user": user}


@router.get("/me")
def get_profile(user: dict = Depends(current_user)):
    return {"user": user}
