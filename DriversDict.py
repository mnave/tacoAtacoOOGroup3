from UserDict import UserDict
from headerRelated import removeHeader
from Time import Time
from constants import *
from Driver import Driver


class DriversDict(UserDict):

    def __init__(self, file_name = None):
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


    def __str__(self):
        output = ""
        for driver in self.values():
            output += driver.getDriverName() + "\n"

        return output

