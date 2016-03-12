# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from UserList import UserList
from Time import Time
from constants import *
from headerRelated import removeHeader
from Service import Service


class ServicesList(UserList):
    """A collection of Services. The behaviour of this collection is similar to the one of the list type"""

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

    def emptyServices(self, drivers, vehicles):
        """Creates an accessory ServicesList to be used in the first working period,
        after attribution of vehicles to the available drivers.


        Requires: drivers and vehicles are collections of drivers and vehicles, respectively.
        Ensures: A ServicesList regarding the working period prior to the first of the day (ie 0709).
        This will be useful if one considers the first working period of the day (0911),
        where vehicles are not attributed to drivers and no service List is available.
        Thus, vehicles, lexicographic sorted by plate, are attributed to drivers
        according to their entry hour. All the service-related information is
        set as a "no service" (_no_client_, _no_circuit_, service kms = 0), Arrival and Departure
        hours are set as the Driver's entry hour and being ready to work,
        drivers' status is standby, of course!
        """

        lstDrivers = []
        lstVehicles = []
        for i in drivers.values():
            lstDrivers.append(i)

        for j in vehicles.values():
            lstVehicles.append(j._plate)

        # sort drivers for the 1st period: 0911
        d = sorted(lstDrivers)
        v = sorted(lstVehicles)

        j = 0
        for i in d:
            driverName = i.getDriverName()
            vehiclePlate = v[j]
            serv = Service(driverName, vehiclePlate, "", i.getDriverEntryHour(), i.getDriverEntryHour(), "", "", "")
            serv.noService()
            self.append(serv)
            j += 1

    def __str__(self):
        """String representation of the ServiceList. Returns the driver's names."""

        output = ""
        for service in self:
            output += service.getServiceDriver() + '\n'

        # returns output without the last newline char
        return output.strip()
