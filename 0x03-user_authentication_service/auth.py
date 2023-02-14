#!/usr/bin/env python3
"""
Authentication system
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
