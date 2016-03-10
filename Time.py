class Time:
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
        return self._hours

    def getMinutes(self):
        return self._minutes

    def setHours(self, hours):
        self._hours = hours

    def setMinutes(self, minutes):
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
        if self.getHours() == other_time.getHours() and self.getMinutes() == other_time.getMinutes():
            return True
        else:
            return False

    def __lt__(self, other_time):
        if self.getHours() < other_time.getHours():
            return True
        elif self.getHours() == other_time.getHours():
            if self.getMinutes() < other_time.getMinutes():
                return True
            else:
                return False
        else:
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
