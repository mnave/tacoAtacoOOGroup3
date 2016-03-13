# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from UserDict import UserDict
from headerRelated import removeHeader
from Time import Time
from constants import *
from Driver import Driver


class DriversDict(UserDict):
    """ Collection of Drivers.
    UserDict works as wrapper for dict objects, allowing to manipulate DriversDict
    object with all the built-in dictionary methods.
    """

    def __init__(self, file_name=None):
        """Creates a DriversDict composed by Driver objects,
        from a file with a list of drivers.

        Requires: If given, file_name is str with the name of a .txt file containing
        a list of drivers organized as in the examples provided in
        the general specification (omitted here for the sake of readability).

        Ensures:
        if file_name is given:
            a DriversDict, composed by objects of class Driver that correspond to the drivers listed
            in file with name file_name.
        if file_name is none:
            a empty DriversList."""

        UserDict.__init__(self)

        if file_name is not None:
            inFile = removeHeader(open(file_name, "r"))
            for line in inFile:
                driverData = line.rstrip().split(", ")
                driverName = driverData.pop(INDEXDriverName)
                driverEntryTime, driverAccumTime = driverData
                driverEntryTime = Time(driverEntryTime)
                driverAccumTime = Time(driverAccumTime)
                newDriver = Driver(driverName, driverEntryTime, driverAccumTime)

                self[driverName] = newDriver

    def __eq__(self, otherDriversDict):
        """Comparison of instances of DriversDict object"""

        if self.__dict__ == otherDriversDict.__dict__:
            return True

        return False

    def __str__(self):
        """
        A string representain of a DriversDict
        """

        output = ""
        for driver in self.values():
            output += driver.getDriverName() + "\n"

        return output

