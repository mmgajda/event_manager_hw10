import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

from pydantic import ValidationError
import pytest
from app.schemas.user_schemas import UserCreate

# Test username validation
@pytest.mark.parametrize("username, is_valid", [
    ("valid_username", True),
    ("in valid", False),
    ("usr", False),  # Assuming your minimum length is above 3
    ("toolongusername" * 5, False),  # Assuming max length is 50
])
def test_username_validation(username, is_valid):
    try:
        user = UserCreate(username=username, email="test@example.com", password="ValidPassword123!")
        assert is_valid  # if no ValidationError, assert must pass for valid usernames
    except ValidationError as e:
        if is_valid:
            pytest.fail(f"Expected username to be valid: {username}")
