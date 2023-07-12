from fastapi import APIRouter, Depends, HTTPException
from typing import Any

from user.schemas import UserCreate, UserRead
from user.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from settings.database import get_async_session
from sqlalchemy import select, insert
from core.security import get_password_hash

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.post("", response_model=UserRead)
async def create_user(
        user: UserCreate,
        session: AsyncSession = Depends(get_async_session)
) -> Any:
    """
    Create new user.
    """
    query_get = select(User).where(User.username == user.username)
    active_user = await session.execute(query_get)
    if active_user.mappings().all():
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    query_insert = insert(User).values(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )
    await session.execute(query_insert)
    await session.commit()
    new_user = await session.execute(query_get)
    new_user = new_user.scalar_one_or_none()
    return UserRead.from_orm(new_user)


@router.get("", response_model=UserRead)
async def get_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(get_async_session)
) -> Any:
    """
    Get a specific user by id.
    """
    query = select(User).where(User.id == user_id)
    data = await session.execute(query)
    user = data.scalar_one_or_none()
    if user:
        return UserRead.from_orm(user)
    raise HTTPException(
        status_code=400, detail={"detail": "No such user found"}
    )
