#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Calendar(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def deleteCalendar(self, calendarID):
        return NotImplemented

    @abstractmethod
    def getCalendar(self, calendarID):
        return NotImplemented

    @abstractmethod
    def insertCalendar(self):
        return NotImplemented

    @abstractmethod
    def updateCalendar(self, calendarID):
        return NotImplemented
