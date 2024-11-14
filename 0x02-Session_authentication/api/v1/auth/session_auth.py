#!/usr/bin/env python3
"""
Session authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    Session authentication class that inherits from Auth.
    It uses a session cookie to manage user authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id=None):
        """
        Creates a session for the user and returns the session ID.
        """
        if user_id is None:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Retrieves the user ID linked to the session ID.
        """
        if session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def session_cookie(self, request=None):
        """
        Retrieves the session cookie from the request.
        """
        if request is None:
            return None
        cookie = request.cookies.get(self.session_name)
        return cookie

    def current_user(self, request=None):
        """
        Retrieves the current user based on the session ID in the request.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Destroys the session of the current user, logging them out.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
