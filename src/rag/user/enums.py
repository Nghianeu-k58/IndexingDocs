"""
Define enums for user.
"""


class Role:
    anonymous = "UNKNOW"
    user = "USER"
    admin = "ADMIN"


class UserField:
    user_id = "user_id"
    email = "email"
    password = "password"
    role = "role"
    name = "name"
    created_date = "created_date"
