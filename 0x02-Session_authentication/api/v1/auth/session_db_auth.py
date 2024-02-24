#!/usr/bin/env python3
"""
Expiration and storage module for api
"""

from datetime import datetime, timedelta
from flask import request

from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Class for Expiration and storage module
    """
    def create_session(self, user_id=None) -> str:
        """
        It creates and stores the session for the user
        """
        session_id = super().create_session(user_id)
        if type(session_id) == str:
            kwargs = {
                'user_id': user_id,
                'session_id': session_id,
            }
            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        IT gets the user is of the user associated with the particular
        session id
        """
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(sessions) <= 0:
            return None
        current_time = datetime.now()
        time_duration = timedelta(seconds=self.session_duration)
        expired_time = session[0].created_at + time_duration
        if expired_time < current_time:
            return None
        return session[0].user_id
    
    def destroy_session(self, request=None) -> bool:
        """
        It damages the authenticated session
        """
        session_id = self.session_cookie(request)
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(sessions) <= 0:
            return False
        sessions[0].remove()
        return True
