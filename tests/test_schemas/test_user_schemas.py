from builtins import str
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]
    # assert user.last_login_at == user_response_data["last_login_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        
        
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

# Tests for UserBase
def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        user = UserBase(**user_base_data_invalid)
    
    assert "value is not a valid email address" in str(exc_info.value)
    assert "john.doe.example.com" in str(exc_info.value)

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

