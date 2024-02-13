#!/usr/bin/env python3
"""
This is Authentication module for the API
"""

from typing import List, TypeVar
import re
from flask import request


class Auth:
    """
    Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        It checks if the path requires authentication
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ""
                if exclusion_path[-1] == "*":
                    pattern = "{}.*".format(exclusion_path[0:-1])
                elif exclusion_path[-1] == "/":
                    pattern_path = "{}/*".format(exclusion_path[0:-1])
                else:
                    pattern = "{}/*".format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        It retrieves the authorization header from the request
        """
        if request is not None:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        It retrieves the current user from the request.
        """
        return None
