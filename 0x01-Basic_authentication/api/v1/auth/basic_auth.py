#!/usr/bin/env python3
"""Representation of BasicAuth class
"""
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic authentication
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extract based64 authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        headers = authorization_header.split()
        if len(headers) != 2:
            return None
        basic, token = headers[0], headers[1]
        if basic != 'Basic':
            return None
        return token

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ decode base64 authorization header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
        except Exception as e:
            return None
        return decoded.decode('utf8')

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header:
            str) -> (str, str):
        """ Extract user credentials
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        email, password = decoded_base64_authorization_header.split(":")
        return (email, password)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Get user Object based on user's email and password
        """
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None
