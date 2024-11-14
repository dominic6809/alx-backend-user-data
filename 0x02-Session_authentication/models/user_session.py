#!/usr/bin/env python3
"""
User Session Model
"""
from models.base import Base
from uuid import uuid4
from datetime import datetime


class UserSession(Base):
    """
    UserSession model that inherits from Base.
    This model stores user session information in a persistent way.
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        Initializes a new UserSession instance with user_id and session_id.
        """
        if kwargs:
            self.user_id = kwargs.get('user_id')
            self.session_id = kwargs.get('session_id')
            self.created_at = kwargs.get('created_at', datetime.now())
        else:
            self.user_id = str(uuid4())
            self.session_id = str(uuid4())
            self.created_at = datetime.now()

        super().__init__(*args, **kwargs)
