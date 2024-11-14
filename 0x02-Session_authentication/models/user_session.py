#!/usr/bin/env python3
"""
User Session Model
"""
from models.base import Base


class UserSession(Base):
    """
    UserSession model that inherits from Base.
    This model stores user session information in a persistent way.
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        Initializes a User session instance.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
