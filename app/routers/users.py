# app/routers/users.py

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.users import UserService
from app.schemas.users import (
    UserCreate,
    UserOut,
    UsersOut,
    UserOutDelete,
    UserUpdate
)
from app.core.security import check_admin_role

# Initialize the router with tags and a prefix
router = APIRouter(tags=["Users"], prefix="/users")

# Get All Users
@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=UsersOut,
    dependencies=[Depends(check_admin_role)]
)
def get_all_users(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    search: str | None = Query("", description="Search based on username"),
    role: str = Query("user", enum=["user", "admin"])
):
    """
    Retrieve all users with pagination, search, and role filtering.
    """
    return UserService.get_all_users(db, page, limit, search, role)

# Get User By ID
@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)]
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific user by their ID.
    """
    return UserService.get_user(db, user_id)

# Create New User
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)]
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new user.
    """
    return UserService.create_user(db, user)

# Update Existing User
@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)]
)
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing user by their ID.
    """
    return UserService.update_user(db, user_id, updated_user)

# Delete User By ID
@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOutDelete,
    dependencies=[Depends(check_admin_role)]
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a specific user by their ID.
    """
    return UserService.delete_user(db, user_id)
