"""
Test for all helper for user services.
"""

from src.rag.user.utils import email_validate, normalize_email


def test_validate_email_successful():
    """Test with validate email successful."""
    email = "test@example.com"
    result, msg = email_validate(email=email)

    assert result is True
    assert msg == "OK"


def test_validate_email_faild():
    """Test with email lack of @ symbol"""
    email = "testexample.com"
    result, msg = email_validate(email=email)

    assert result is False
    assert msg == 'Email must contains "@" symbol.'


def test_valid_email_faild_more_symbol():
    """Test with email contains more than 2 @ symbols."""
    email = "tes@t@example.com"
    result, msg = email_validate(email=email)

    assert result is False
    assert msg == 'Email contains more than one "@" symbol.'


def test_validate_email_with_space():
    """Test with email contains space."""
    email = "test email@eample.com"
    result, msg = email_validate(email=email)

    assert result is False
    assert msg == "Email will not contain spaces."


def test_email_to_long():
    """Test with email to long."""
    prefix = "a" * 256
    email = f"{prefix}@example.com"

    result, msg = email_validate(email=email)

    assert result is False
    assert msg == "The email is over 256 letters."


def test_email_start_with_number():
    """Test with email start with number."""
    email = "123@example.com"
    result, msg = email_validate(email=email)

    assert result is False
    assert msg == "The email start with number."


def test_normalize_email():
    """Test normalize email."""
    emails = [
        ["test1@EXAMPLE.com", "test1@example.com"],
        ["Test2@Example.com", "Test2@example.com"],
        ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
        ["test4@example.COM", "test4@example.com"],
    ]

    for email, expected_email in emails:
        assert expected_email == normalize_email(email=email)
