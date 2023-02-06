#!/usr/bin/env python3
"""Representation of BasicAuth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Basic - Base64 part
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
