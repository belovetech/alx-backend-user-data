#!/usr/bin/env python3
"""Representation of session authentication class
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session id for user
        """
        if user_id and isinstance(user_id, str):
            session_id = uuid.uuid4()
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None
