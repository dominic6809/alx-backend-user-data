#!/usr/bin/env python3
"""
This module defines the BasicAuth class for handling basic authentication.
"""

import re
import base64
import binascii
from typing import Tuple, TypeVar
from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    Basic Authentication class that handles authorization via Basic Auth.
    Inherits from the Auth class.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract the Base64 string from the Authorization header.

        Returns:
            The Base64 part of the Authorization header if valid, otherwise None.
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decode the Base64 string to get the decoded authorization header.

        Returns:
            The decoded string if valid, otherwise None.
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_value = base64.b64decode(base64_authorization_header).decode("utf-8")
        except Exception:
            return None

        return decoded_value

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract the user email and password from the decoded Base64 Authorization header.

        Handles passwords with colons.

        Returns:
            tuple: A tuple containing the email and password if valid, otherwise (None, None).
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return None, None

        parts = decoded_base64_authorization_header.split(":", 1)

        if len(parts) != 2:
            return None, None

        email, password = parts
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieve the user instance based on the provided email and password.

        Returns:
            User instance if credentials are valid, otherwise None.
        """
        if (user_email is None or not isinstance(user_email, str) or
                user_pwd is None or not isinstance(user_pwd, str)):
            return None

        user = User.search({"email": user_email})

        if user is None or not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for the current request using Basic Auth.

        Returns:
            User instance if authenticated, otherwise None.
        """
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_authorization_header = self.extract_base64_authorization_header(authorization_header)
        if base64_authorization_header is None:
            return None

        decoded_base64_authorization_header = self.decode_base64_authorization_header(base64_authorization_header)
        if decoded_base64_authorization_header is None:
            return None

        email, password = self.extract_user_credentials(decoded_base64_authorization_header)
        if email is None or password is None:
            return None

        user = self.user_object_from_credentials(email, password)
        return user
