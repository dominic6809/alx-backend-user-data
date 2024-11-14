#!/usr/bin/env python3
"""
Session DB Authentication Class
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
import os


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class that inherits from SessionExpAuth.
    This class stores sessions in a database (or file) instead of in memory.
    """

    def create_session(self, user_id=None):
        """
        Creates a session and stores it in the database.
        Returns the session ID.
        """
        # Create session using SessionExpAuth's create_session
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Create a new UserSession instance
        session = UserSession(user_id=user_id, session_id=session_id, created_at=datetime.now())
        session.save()  # Assuming save method stores it in a database/file
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the user ID for the given session_id if the session is valid.
        """
        if session_id is None:
            return None

        # Retrieve the session from the database (or file)
        session = UserSession.search({"session_id": session_id})
        if not session:
            return None

        session = session[0]
        # Check if the session has expired
        if self.session_duration > 0 and session.created_at + timedelta(seconds=self.session_duration) < datetime.now():
            return None

        return session.user_id

    def destroy_session(self, request=None):
        """
        Destroys the session by removing the UserSession from the database.
        """
        session_id = request.cookies.get(self.session_name)
        if session_id is None:
            return False

        session = UserSession.search({"session_id": session_id})
        if not session:
            return False

        # Delete the session from the database (or file)
        session[0].remove()  # Assuming remove method deletes it
        return True
