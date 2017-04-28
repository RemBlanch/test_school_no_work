#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Google's OAuth 2.0 API TOKEN AUTHORIZATION

    IMPORTANT: OAuth 2 requires HTTPS. This app will override that if DEBUG is
    set in the environment.
"""
from abc import ABCMeta, abstractmethod

class token_authorization(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def authorization(self):
        return NotImplemented

    @abstractmethod
    def retrieve_token(self):
        return NotImplemented

    @abstractmethod
    def automatic_refresh_token(self):
        pass

    @abstractmethod
    def manual_refresh(self):
        pass

    @abstractmethod
    def token_validate(self):
        return NotImplemented

    @abstractmethod
    def token_revoke(self):
        return NotImplemented
