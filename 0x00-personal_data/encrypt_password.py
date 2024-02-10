#!/usr/bin/env python3
"""
Module for encrypting passwords.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    It put all passwords in hashes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    It verify whether hashed password was formed from the given password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
