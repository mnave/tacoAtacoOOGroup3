#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


class Driver(object):
    """Driver of a tuk tuk from Taco-a-Taco"""

    def __init__(self, Name, EntryHour, AccumTime):
        """Creates a new driver.

        Requires: Name is a string representing the name of driver. EntryHour and AccumTime are strings represeting time
        in the format "HH:MM". EntryHour represents the the drivers's entry hour and AccumTime represents the driver's
        accumulated time since the beggining of the workday.
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

        Requires: EntryHour is a string represeting time in the format "HH:MM".
        Ensures: self.getDriverEntryHour() == EntryHour.
        """

        self._entryHour = EntryHour

    def setDriverAccumTime(self, AccumTime):
        """Set the accumulated time of the driver.

        Requires: AccumTime is a string represeting time in the format "HH:MM".
        Ensures: self.getDriverAccumTime() == AccumTime.
        """

        self._accumTime = AccumTime
