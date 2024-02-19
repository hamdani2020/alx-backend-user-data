#!/usr/bin/env python3
"""
Expiration module for API
"""

from datetime import datetime, timedelta
import os
from flask import request
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    Expiration authentication class
    """
    def __init__(self) -> None:
        """
        It initializes the new SessionExpAuth instance
        """
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        It creates a session id for the usere
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
        It gets the user id associated with the given session
        """
        if session_id in self.user_id_by_session_id:
            session_dict = self.usere_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' not in session_dict:
                return None
            cur_time = datetime.now()
            time_spent = timedelta(seconds=self.session_duration)
            expired_time = session_dict['created_at'] + time_spent
            if expired_time < cur_time:
                return None
            return session_dict['user_id']
