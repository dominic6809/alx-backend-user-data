#!/usr/bin/env python3
"""
User model module
Defines the User SQLAlchemy model for the users table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model mapped to the users table in the database.

    Attributes:
        id (int): Primary key, an integer unique to each user.
        email (str): User's email, a non-nullable string.
        hashed_password (str): User's hashed password, a non-nullable string.
        session_id (str): Session ID, nullable string.
        reset_token (str): Reset token, nullable string.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
