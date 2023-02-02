#!/usr/bin/env python3
"""Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bcrypt:
    """Hash password using bcrypt
    """
    salt = bcrypt.gensalt()
    password_byte = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(password_byte, salt)
    return hashed
