from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from httpx import AsyncClient

from core.security import get_password_hash
from user.models import User
from user.schemas import UserRead
from test.utils.utils import random_email, random_lower_string, random_username


async def test_api_route_create_user_without_email(ac: AsyncClient) -> None:
    username = random_username()
    password = get_password_hash(random_lower_string())

    response = await ac.post(
        "/user",
        headers={"accept": "application/json"},
        json={
            "username": username,
            "password": password
        }
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": username, "email": None}


async def test_api_route_create_user_with_email(ac: AsyncClient) -> None:
    username = random_username()
    password = get_password_hash(random_lower_string())
    email = random_email()

    response = await ac.post(
        "/user",
        headers={"accept": "application/json"},
        json={
            "username": username,
            "password": password,
            "email": email
        }
    )
    assert response.status_code == 200
    assert response.json() == {"id": 2, "username": username, "email": email}


async def test_api_route_create_user_with_wrong_email(ac: AsyncClient) -> None:
    username = random_username()
    password = get_password_hash(random_lower_string())
    email = "email.com"

    response = await ac.post(
        "/user",
        headers={"accept": "application/json"},
        json={
            "username": username,
            "password": password,
            "email": email
        }
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
              "loc": [
                "body",
                "email"
              ],
              "msg": "value is not a valid email address",
              "type": "value_error.email"
            }
        ]
    }


async def test_api_route_create_user_with_exist_username(ac: AsyncClient, db: AsyncSession) -> None:
    query_get = select(User).where(User.id == 1)
    user = await db.execute(query_get)
    await db.commit()
    user = user.scalar_one_or_none()

    username = user.username
    password = get_password_hash(random_lower_string())
    email = random_email()

    response = await ac.post(
        "/user",
        headers={"accept": "application/json"},
        json={
            "username": username,
            "password": password,
            "email": email
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "The user with this username already exists in the system."}


async def test_api_route_get_user_by_id(ac: AsyncClient, db: AsyncSession) -> None:
    query_get = select(User).where(User.id == 1)
    user = await db.execute(query_get)
    await db.commit()
    user = user.scalar_one_or_none()

    response = await ac.get(
        "/user",
        headers={"accept": "application/json"},
        params={
            "user_id": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == UserRead.from_orm(user)


async def test_api_route_get_user_by_wrong_id(ac: AsyncClient) -> None:
    response = await ac.get(
        "/user",
        headers={"accept": "application/json"},
        params={
            "user_id": 3
        }
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": {
            "detail": "No such user found"
        }
    }


