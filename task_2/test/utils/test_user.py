from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from user.models import User
from user.schemas import UserCreate
from core.security import get_password_hash
from test.utils.utils import random_email, random_lower_string, random_username


async def test_create_user_without_email(db: AsyncSession) -> None:
    username = random_username()
    password = get_password_hash(random_lower_string())
    user_in = UserCreate(username=username, password=password)

    query_insert = insert(User).values(**user_in.dict())
    query_get = select(User).where(User.username == user_in.username)
    await db.execute(query_insert)
    await db.commit()

    new_user = await db.execute(query_get)
    await db.commit()
    new_user = new_user.scalar_one_or_none()
    assert new_user.username == username
    assert new_user.email is None
    assert hasattr(new_user, "password")


async def test_create_user_with_email(db: AsyncSession) -> None:
    username = random_username()
    password = get_password_hash(random_lower_string())
    email = random_email()
    user_in = UserCreate(username=username, email=email, password=password)

    query_insert = insert(User).values(**user_in.dict())
    query_get = select(User).where(User.username == user_in.username)
    await db.execute(query_insert)
    await db.commit()

    new_user = await db.execute(query_get)
    await db.commit()
    new_user = new_user.scalar_one_or_none()
    assert new_user.username == username
    assert new_user.email == email
    assert hasattr(new_user, "password")
