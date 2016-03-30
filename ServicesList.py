# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from UserList import UserList
from Service import Service
from TimeTT import Time
from FileUtil import *


class ServicesList(UserList):
    """A collection of Services. The behaviour of this collection is similar to the one of the list type"""

    # Index of element with driver's name in a line of a services file
    INDEXDriverName = 0

    # Index of element with vehicle's plate in a line of a services file
    INDEXVehiclePlate = 1

    # Index of element with clients's name in a line of a services file
    INDEXClientName = 2

    # Index of departure hour in a line of a services file
    INDEXDepartureHour = 3

    # Index of arrival hour in a line of a services file
    INDEXArrivalHour = 4

    # Index of circuit id in a line of a services file
    INDEXCircuitId = 5

    # Index of circuit kms in a line of a services file
    INDEXCircuitKms = 6

    # Index of driver's status in a line of a services file
    INDEXDriverStatus = 7

    # Index of driver's accumlated time in a line of a services file
    INDEXAccumulatedTime = 8

    # Index of element with car's autonomy in kms in a line of a services file
    INDEXINDEXVehicAutonomy = 9

    # Index of element with accumulated kms in a line of a services file
    INDEXAccumulatedKms = 10

    def __init__(self, file_name=None):
        """Creates a ServicesList composed by Services objects,
        from a file with a list of services.

        Requires: If given, file_name is str with the name of a .txt file containing
        a list of services organized as in the examples provided in
        the general specification (omitted here for the sake of readability).
        Ensures:
        if file_name is given:
            a ServiceList, composed by objects of class Service that correspond to the services listed
            in file with name file_name. In this ServiceList, drivers terminating their services earlier
            have priority over the ones terminating later; lexicographic order of drivers's names
            decides eventual ties in each case above.
        if file_name is none:
            a empty ServiceList.
        """

        # creates empty ServicesList
        UserList.__init__(self)

        # if file_name is given, self is populated with Services corresponding to the
        # services on the file file_name
        if file_name is not None:
            inFile = FileUtil(file_name)

            for line in inFile.getContent():
                servData = line.rstrip().split(", ")
                servDriver = servData[ServicesList.INDEXDriverName]
                servPlate = servData[ServicesList.INDEXVehiclePlate]
                servClient = servData[ServicesList.INDEXClientName]
                servDeparTime = Time(servData[ServicesList.INDEXDepartureHour])
                servArrivalTime = Time(servData[ServicesList.INDEXArrivalHour])
                servCircuit = servData[ServicesList.INDEXCircuitId]
                servCircuitKms = servData[ServicesList.INDEXCircuitKms]
                servDriverStatus = servData[ServicesList.INDEXDriverStatus]
                newService = Service(servDriver, servPlate, servClient, servDeparTime, servArrivalTime, \
                                     servCircuit, servCircuitKms, servDriverStatus)
                self.append(newService)

    def emptyServices(self, drivers, vehicles):
        """Creates an accessory ServicesList to be used in the first working period,
        after attribution of vehicles to the available drivers.


        Requires: drivers and vehicles are collections of drivers and vehicles, respectively.
        Ensures: A ServicesList regarding the working period prior to the first of the day (ie 0709).
        This will be useful if one considers the first working period of the day (0911),
        where vehicles are not attributed to drivers and no service List is available.
        Thus, vehicles, lexicographic sorted by plate, are attributed to drivers
        according to their entry hour (and name, in case of tie). All the service-related information is
        set as a "no service" (_no_client_, _no_circuit_, service kms = 0), Arrival and Departure
        hours are set as the Driver's entry hour and being ready to work,
        drivers' status is standby, of course!
        """

        # sort drivers for the 1st period (0911) according to Drivers' EntryHour
        # and in case of tie, Drivers' name
        d = sorted(drivers.values())
        v = sorted(vehicles.keys())

        j = 0
        for i in d:
            driverName = i.getDriverName()
            vehiclePlate = v[j]
            serv = Service(driverName, vehiclePlate, "", i.getDriverEntryHour(), i.getDriverEntryHour(), "", "", "")
            serv.noService()
            self.append(serv)
            j += 1

    def __eq__(self, other_ServicesList):
        pass

    def __str__(self):
        """String representation of the ServiceList. Returns the driver's names."""

        output = ""
        for service in self:
            output += service.getServiceDriver() + '\n'

        # returns output without the last newline char
        return output.strip()
