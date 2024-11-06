#!/usr/bin/env python3
"""
Module for password encryption and validation.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with salt.

    Args:
        password (str): The password string to be hashed.

    Returns:
        bytes: The salted, hashed password.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a provided password matches the stored hashed password.

    Args:
        hashed_password (bytes): The stored hashed password.
        password (str): The password string to check.

    Returns:
        bool: True if the password is correct, False otherwise.
    """
    # Use bcrypt to check if the provided password matches the hashed one
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
