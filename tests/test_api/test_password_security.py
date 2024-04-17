import pytest
from sqlalchemy.future import select
from httpx import AsyncClient
from app.main import app
from app.models.user_model import User
from app.utils.security import verify_password  

@pytest.fixture(scope="function")
async def async_client():
    """Fixture to provide an HTTP client for interacting with the FastAPI app."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_password_hashing_and_storage(async_client, db_session):
    form_data = {
        "username": "admin",
        "password": "secret",
    }
    # Login and get the access token
    token_response = await async_client.post("/token", data=form_data)
    access_token = token_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}

    user_data = {
        "username": "secureuser",
        "email": "secure@example.com",
        "password": "sS#fdasrongPassword123!",
    }

    # Create user via the API
    response = await async_client.post("/users/", json=user_data, headers=headers)
    assert response.status_code == 201

    user_id = response.json()["id"]

    # Fetch the user from the database to verify password hashing
    async with db_session as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar()

    assert user is not None
    # Validate that the password is hashed correctly and does not match plaintext
    assert user.hashed_password != user_data['password']
    # Using the security utility to verify the hashed password
    assert verify_password(user_data['password'], user.hashed_password), "Password hashing failed"