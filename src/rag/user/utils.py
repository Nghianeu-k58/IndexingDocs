"""
Define all helper function for user services.
"""
import re


def email_validate(email: str):
    """Validating email."""
    # validate length
    if len(email) > 256:
        return False, "The email is over 256 letters."

    # validate symbol
    if not re.search(r"@", email):
        return False, 'Email must contains "@" symbol.'

    if len(email.split("@")) > 2:
        return False, 'Email contains more than one "@" symbol.'

    # check space
    if re.search(r"\s+", email):
        return False, "Email will not contain spaces."

    # check digist
    if email[0].isdigit():
        return False, "The email start with number."

    return True, "OK"


def normalize_email(email):
    """Normalize and return email."""
    parts = email.split("@")
    return f"{parts[0]}@{parts[1].lower()}"
