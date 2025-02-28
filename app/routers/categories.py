# app/routers/categories.py

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.categories import CategoryService
from app.schemas.categories import (
    CategoryCreate,
    CategoryOut,
    CategoriesOut,
    CategoryOutDelete,
    CategoryUpdate
)
from app.core.security import check_admin_role

# Initialize the router with tags and a prefix
router = APIRouter(tags=["Categories"], prefix="/categories")

# Get All Categories
@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=CategoriesOut
)
def get_all_categories(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    search: str | None = Query("", description="Search based on the name of categories")
):
    """
    Retrieve all categories with pagination and optional search.
    """
    return CategoryService.get_all_categories(db, page, limit, search)

# Get Category By ID
@router.get(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut
)
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific category by its ID.
    """
    return CategoryService.get_category(db, category_id)

# Create New Category
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryOut,
    dependencies=[Depends(check_admin_role)]
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new category.
    """
    return CategoryService.create_category(db, category)

# Update Existing Category
@router.put(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut,
    dependencies=[Depends(check_admin_role)]
)
def update_category(
    category_id: int,
    updated_category: CategoryUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing category by its ID.
    """
    return CategoryService.update_category(db, category_id, updated_category)

# Delete Category By ID
@router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOutDelete,
    dependencies=[Depends(check_admin_role)]
)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a specific category by its ID.
    """
    return CategoryService.delete_category(db, category_id)
