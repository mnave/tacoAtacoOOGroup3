from UserList import UserList
from Time import Time
from constants import *
from headerRelated import removeHeader
from Service import Service


class ServicesList(UserList):

    def __init__(self, file_name=None):
        UserList.__init__(self)

        if file_name is not None:
            inFile = removeHeader(open(file_name, "r"))

            for line in inFile:
                servData = line.rstrip().split(", ")
                servDriver = servData[INDEXDriverName]
                servPlate = servData[INDEXVehiclePlate]
                servClient = servData[INDEXClientName]
                servDeparTime = Time(servData[INDEXDepartureHour])
                servArrivalTime = Time(servData[INDEXArrivalHour])
                servCircuit = servData[INDEXCircuitId]
                servCircuitKms = servData[INDEXCircuitKms]
                servDriverStatus = servData[INDEXDriverStatus]
                newService = Service(servDriver, servPlate, servClient, servDeparTime, servArrivalTime, \
                                     servCircuit, servCircuitKms, servDriverStatus)
                self.append(newService)




