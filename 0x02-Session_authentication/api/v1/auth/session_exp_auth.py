#!/usr/bin/env python3
"""
Session expiration authentication class
"""
from datetime import datetime, timedelta
import os
from api.v1.auth.session_auth import SessionAuth

class SessionExpAuth(SessionAuth):
    """
    Session expiration authentication class that inherits from SessionAuth.
    This class adds session expiration logic based on SESSION_DURATION.
    """
    def __init__(self):
        """
        Initializes the session expiration class with session duration from environment.
        """
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION", 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Creates a session ID with expiration date.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Store the session dictionary with created_at as the current datetime
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns user_id for a session if it is valid and not expired.
        """
        if session_id is None:
            return None

        session_data = self.user_id_by_session_id.get(session_id)
        if not session_data:
            return None

        # If session_duration is 0 or less, the session does not expire
        if self.session_duration <= 0:
            return session_data["user_id"]

        created_at = session_data.get("created_at")
        if not created_at:
            return None

        # Check if the session has expired
        if created_at + timedelta(seconds=self.session_duration) < datetime.now():
            return None

        return session_data["user_id"]
