import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

# Fixtures for common test data
@pytest.fixture
def user_base_data():
    return {
        "username": "john_doe_123",
        "email": "john.doe@example.com",
        "full_name": "John Doe",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg"
    }

@pytest.fixture
def user_create_data(user_base_data):
    return {**user_base_data, "password": "SecurePassword123!"}

@pytest.fixture
def user_update_data():
    return {
        "email": "john.doe.new@example.com",
        "full_name": "John H. Doe",
        "bio": "I specialize in backend development with Python and Node.js.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe_updated.jpg"
    }

@pytest.fixture
def user_response_data():
    return {
        "id": "unique-id-string",
        "username": "testuser",
        "email": "test@example.com",
        "last_login_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "links": []
    }

@pytest.fixture
def login_request_data():
    return {"username": "john_doe_123", "password": "SecurePassword123!"}

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.username == user_base_data["username"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.username == user_create_data["username"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_partial(user_update_data):
    partial_data = {"email": user_update_data["email"]}
    user_update = UserUpdate(**partial_data)
    assert user_update.email == partial_data["email"]

# Tests for UserResponse
def test_user_response_datetime(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.last_login_at == user_response_data["last_login_at"]
    assert user.created_at == user_response_data["created_at"]
    assert user.updated_at == user_response_data["updated_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.username == login_request_data["username"]
    assert login.password == login_request_data["password"]

# Parametrized tests for username and email validation
@pytest.mark.parametrize("username", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_username_valid(username, user_base_data):
    user_base_data["username"] = username
    user = UserBase(**user_base_data)
    assert user.username == username

@pytest.mark.parametrize("username", ["test user", "test?user", "", "us"])
def test_user_base_username_invalid(username, user_base_data):
    user_base_data["username"] = username
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)
        
        
""" Start of added tests - MMG """
# Parametrized tests for username length and special character(s) validation

@pytest.mark.parametrize("username, valid", [
    ("a"*51, False),  # Exceeding max length
    ("ab", False),    # Below min length
    ("valid_username", True),
    ("invalid_username?", False),  # Invalid character
    ("another-valid_username123", True)
])
def test_username_validation(username, valid, user_create_data):
    user_create_data["username"] = username
    if valid:
        user = UserCreate(**user_create_data)
        assert user.username == username
    else:
        with pytest.raises(ValidationError):
            UserCreate(**user_create_data)

# Parametrized tests for email format validation

@pytest.mark.parametrize("email, valid", [
    ("email@example.com", True),
    ("not-an-email", False),
    ("another.email@example.co", True),
    ("invalid-email@", False)
])
def test_email_validation(email, valid, user_create_data):
    user_create_data["email"] = email
    if valid:
        user = UserCreate(**user_create_data)
        assert user.email == email
    else:
        with pytest.raises(ValidationError):
            UserCreate(**user_create_data)
            
# Parametrized tests for picture format and picture URL validation 

@pytest.mark.parametrize("url, valid", [
    ("https://example.com/profile.jpg", True),
    ("https://example.com/profile.jpeg", True),
    ("https://example.com/profile.png", True),
    ("https://example.com/profile.bmp", False),  # Assuming only jpg, jpeg, and png are valid
    ("https://example.com/", False),
    ("", False)  # Assuming the URL cannot be empty
])
def test_profile_picture_url_validation(url, valid, user_create_data):
    user_create_data["profile_picture_url"] = url
    if valid:
        user = UserCreate(**user_create_data)
        assert user.profile_picture_url == url
    else:
        with pytest.raises(ValidationError):
            UserCreate(**user_create_data)

