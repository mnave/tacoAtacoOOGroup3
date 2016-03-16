# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from Time import Time


class Driver(object):
    """Driver of a tuk tuk from Taco-a-Taco"""

    # Status of driver with no time left in the day
    STATUSTerminated = "terminates"

    # Status of car charging battery
    STATUSCharging = "charges"

    # Status of driver waiting for next service
    STATUSStandBy = "standby"

    # Limit of driver's daily allowed time to drive
    TIMELimit = Time("05:00")

    # Limit of driver's daily allowed time left to be able
    # to be assigned a next service
    TIMEThreshold = Time("00:30")

    def __init__(self, Name, EntryHour, AccumTime):
        """Creates a new driver.

        Requires: Name is a string representing the name of driver. EntryHour and AccumTime are Time objects.
        EntryHour represents the the drivers's entry hour and AccumTime represents the driver's accumulated time
        since the beggining of the workday.
        Ensures: Creation of a new Driver object.
        """
        self._name = Name
        self._entryHour = EntryHour
        self._accumTime = AccumTime

    def getDriverName(self):
        """The driver's name."""

        return self._name

    def getDriverEntryHour(self):
        """The drivers's entry hour."""

        return self._entryHour

    def getDriverAccumTime(self):
        """The drivers accumulated time since the beggining of the workday."""

        return self._accumTime

    def setDriverName(self, Name):
        """Set the name of the driver.

        Requires: Name is a string.
        Ensures: self.getDriverName() == Name
        """

        self._name = Name

    def setDriverEntryHour(self, EntryHour):
        """Set the entry hour of the driver.

        Requires: EntryHour is a Time object.
        Ensures: self.getDriverEntryHour() == EntryHour.
        """

        self._entryHour = EntryHour

    def setDriverAccumTime(self, AccumTime):
        """Set the accumulated time of the driver.

        Requires: AccumTime is a Time object.
        Ensures: self.getDriverAccumTime() == AccumTime.
        """

        self._accumTime = AccumTime

    def __eq__(self, other_driver):
        """Returns True if self and other_driver names are equal. False otherwise."""

        if self.getDriverName() == other_driver.getDriverName():
            return True

        return False

    def __lt__(self, other_driver):
        """Returns True if self entry hour is smaller than other_driver entry hour. If they are the same,
        returns True if self driver name is lexicographically smaller than other_driver name. False otherwise."""

        if self.getDriverEntryHour() < other_driver.getDriverEntryHour():
            return True
        else:
            if self.getDriverName() < other_driver.getDriverName():
                return True

        return False

    def __str__(self):
        """A string representation of a driver"""

        return "Name: " + self.getDriverName() + "\n" + \
               "Entry Hour: " + self.getDriverEntryHour() + "\n" + \
               "Accumulated Time: " + self.getDriverAccumTime()
