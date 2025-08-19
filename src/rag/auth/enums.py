"""
Define enums for auth.
"""


class UserInfo:
    email = "email"
    password = "password"


class TokenFields:
    email = "sub"
    user_id = "id"
    express = "exp"
    role = "role"
