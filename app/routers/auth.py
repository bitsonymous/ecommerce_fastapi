# app/routers/auth.py

from fastapi import APIRouter, Depends, status, Header
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.services.auth import AuthService
from app.db.database import get_db
from app.schemas.auth import UserOut, Signup

# Initialize the router with tags and a prefix
router = APIRouter(tags=["Auth"], prefix="/auth")

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def user_signup(
    user: Signup,
    db: Session = Depends(get_db)
):
    """
    Sign up a new user.
    """
    return await AuthService.signup(db, user)

@router.post("/login", status_code=status.HTTP_200_OK)
async def user_login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Log in an existing user and return an access token.
    """
    return await AuthService.login(user_credentials, db)

@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh_access_token(
    refresh_token: str = Header(...),  # Make the header parameter required
    db: Session = Depends(get_db)
):
    """
    Refresh the access token using a valid refresh token.
    """
    return await AuthService.get_refresh_token(token=refresh_token, db=db)
