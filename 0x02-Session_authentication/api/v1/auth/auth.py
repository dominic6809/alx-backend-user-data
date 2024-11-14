#!/usr/bin/env python3
"""
This module defines the Auth class for managing API authentication.
"""

import re
from typing import List, TypeVar
from flask import request


class Auth:
    """
    A template for an authentication system.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication.
        Currently returns False by default.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]):
            Paths that are excluded from authentication.

        Returns:
            bool: False, as a placeholder implementation.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        Currently returns None by default.

        Args:
            request: The Flask request object.

        Returns:
            str: None, as a placeholder implementation.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.
        Currently returns None by default.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): None, as a placeholder implementation.
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
        Gets the value of the cookie named SESSION_NAME.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
