#!/usr/bin/env python3
"""Encrypting passwords and validate password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash password using bcrypt
    """
    salt = bcrypt.gensalt()
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check valid password
    validate that the provided password matches the hashed password.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
