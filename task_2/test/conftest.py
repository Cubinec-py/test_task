import pytest
import asyncio

from typing import AsyncGenerator
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from settings.database import metadata, get_async_session, Base
from settings.project import Settings
from main import app
from user.models import User

DATABASE_URL_TEST = Settings.TEST_DATABASE_URL

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
override_async_session_maker = sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(autouse=True, scope="session")
async def db() -> AsyncGenerator[AsyncSession, None]:
    async with override_async_session_maker() as session:
        yield session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# SETUP
@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True, scope="session")
def override_dependency(db: AsyncSession) -> None:
    app.dependency_overrides[get_async_session] = lambda: db


@pytest.fixture(autouse=True)
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test/api/v1") as ac:
        yield ac
