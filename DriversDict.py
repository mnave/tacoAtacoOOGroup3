from UserDict import UserDict
from headerRelated import removeHeader
from Time import Time
from constants import *
from Driver import Driver


class DriversDict(UserDict):
    ''' Collection of Drivers.
    UserDict works as wrapper for dict objects, allowing to manipulate DriversDict
    object with all the built-in dictionary methods.

    Requires: a driverXXYY.txt. In case of file_name = None, can be initiated
    through the UserDict constructor.
    All dictionary methods are inherited and thus, DriversDict works as a subclass of UserDict.

    Ensures: Each object is a dict with all the information regarding one driver.
    DriversDict key corresponds to Drivers' name, and values to the remaining information
    that one can find in each line of the driversXXYY.txt.
    '''

    def __init__(self, file_name=None):
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
        '''
        str method for printing purposes
        '''


        output = ""
        for driver in self.values():
            output += driver.getDriverName() + "\n"

        return output

