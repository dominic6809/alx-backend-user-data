#!/usr/bin/env python3
"""
Session expiration authentication class
"""
import os
from flask import request
from datetime import datetime, timedelta

from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    Session expiration authentication class
    that inherits from SessionAuth.
    This class adds session expiration logic based on SESSION_DURATION.
    """
    def __init__(self):
        """
        Initializes the session expiration class
        with session duration from environment.
        """
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Creates a session ID with expiration date.
        """
        session_id = super().create_session(user_id)
        if type(session_id) != str:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """
        Returns user_id for a session if it is valid and not expired.
        """
        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' not in session_dict:
                return None
            cur_time = datetime.now()
            time_span = timedelta(seconds=self.session_duration)
            exp_time = session_dict['created_at'] + time_span
            if exp_time < cur_time:
                return None
            return session_dict['user_id']
