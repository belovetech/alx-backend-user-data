#!/usr/bin/env python3
"""Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bcrypt:
    """Hash password using bcrypt
    """
    salt = bcrypt.gensalt()
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, salt)
    return hashed
