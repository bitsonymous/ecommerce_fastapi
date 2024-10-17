# app/routers/accounts.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.database import get_db
from app.services.accounts import AccountService
from app.schemas.accounts import AccountOut, AccountUpdate

# Initialize the router with tags and a prefix
router = APIRouter(tags=["Account"], prefix="/me")
auth_scheme = HTTPBearer()  # Create an instance of HTTPBearer for authentication

@router.get("/", response_model=AccountOut)
def get_my_info(
    db: Session = Depends(get_db),  # Dependency injection for the database session
    token: HTTPAuthorizationCredentials = Depends(auth_scheme)  # Dependency for token
):
    """
    Get information about the authenticated user.
    """
    user_info = AccountService.get_my_info(db, token)
    if not user_info:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info


@router.put("/", response_model=AccountOut)
def edit_my_info(
    updated_user: AccountUpdate,
    db: Session = Depends(get_db),  # Dependency injection for the database session
    token: HTTPAuthorizationCredentials = Depends(auth_scheme)  # Dependency for token
):
    """
    Edit information for the authenticated user.
    """
    user_info = AccountService.edit_my_info(db, token, updated_user)
    if not user_info:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info


@router.delete("/", response_model=AccountOut)
def remove_my_account(
    db: Session = Depends(get_db),  # Dependency injection for the database session
    token: HTTPAuthorizationCredentials = Depends(auth_scheme)  # Dependency for token
):
    """
    Remove the authenticated user's account.
    """
    user_info = AccountService.remove_my_account(db, token)
    if not user_info:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info
