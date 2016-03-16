# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


class Time:
    """A representation of time"""

    def __init__(self, time=None):
        """Creates a new time.

        Requires: time is a str with the formar HH:MM.
        Returns: an object of class Time"""

        if time is None:
            pass
        else:
            t = time.split(":")
            self._hours = int(t[0])
            self._minutes = int(t[1])

    def getHours(self):
        """Hours of Time"""

        return self._hours

    def getMinutes(self):
        """Minutes of Time"""

        return self._minutes

    def setHours(self, hours):
        """Changes hours of Time.

        Requires: hours is an int and hours >= 0 and hours < 24
        Ensures: self.getHours() == hours"""

        self._hours = hours

    def setMinutes(self, minutes):
        """Changes minutes of Time.

        Requires: minutes is an int and minutes >= 0 and hours < 60
        Ensurse: self.getMinutes() = minutes"""

        self._minutes = minutes

    def add(self, other_time):
        """The result of the addition of the two times in the arguments.

        Requires: other_time is a Time object.
        Ensures: result of the addition of self with other_time
        """

        result = Time()

        hours = (self.getMinutes() + other_time.getMinutes()) / 60
        M = (self.getMinutes() + other_time.getMinutes()) % 60

        H = self.getHours() + other_time.getHours() + hours

        result.setHours(H)
        result.setMinutes(M)

        return result

    def diff(self, other_time):
        """The result of the subtraction of the two times in the arguments.

        Requires: other_time is a Time object.
        Ensures: result of the subtraction of self with other_time
        """
        result = Time()

        H = self.getHours() - other_time.getHours()
        minutes = self.getMinutes() - other_time.getMinutes()
        M = abs(minutes)

        if minutes < 0:
            H = H - 1
            M = 60 - M

        if H < 0:
            H = 0
            M = 0

        result.setHours(H)
        result.setMinutes(M)

        return result

    def __eq__(self, other_time):
        """Method for testing equality betweeen Times

        Requires: other_time is a Time object.
        Ensures: returns True if minutes and hours of self and other_time are equal. False otherwise."""

        if self.getHours() == other_time.getHours() and self.getMinutes() == other_time.getMinutes():
            return True

        return False

    def __lt__(self, other_time):
        """Method for comparing Times.

        Requires: other_time is a Time object.
        Ensures. returns True if hour of self is lower than time of other_time. If the hours are equal,
        returns True if minutes of self are lower than minutes of other_time. False otherwise."""

        if self.getHours() < other_time.getHours():
            return True
        elif self.getHours() == other_time.getHours():
            if self.getMinutes() < other_time.getMinutes():
                return True

        return False

    def __le__(self, other_time):

        if self < other_time:
            return True
        elif self == other_time:
            return True
        else:
            return False

    def __str__(self):
        """String representation of self, in the format "HH:MM"""

        result = ""

        hours = str(self.getHours())
        minutes = str(self.getMinutes())

        if len(hours) == 1:
            result += "0" + hours
        else:
            result += hours

        result += ":"

        if len(minutes) == 1:
            result += "0" + minutes
        else:
            result += minutes

        return result
