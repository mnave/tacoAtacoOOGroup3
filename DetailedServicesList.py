# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from UserList import UserList
from DetailedService import DetailedService
from copy import deepcopy
from ServicesList import ServicesList
from constants import *
from Time import Time
from Driver import Driver


class DetailedServicesList(UserList):
    """A collection of DetailedServices.
    The behaviour of this collection is similar to the one of the list type"""

    def __init__(self, drivers=None, vehicles=None, services=None):
        """Creates a new DetailedServicesList composed by DetailedServices that
        are extensions of Services with more information about the driver and vehicles.

        Requires: drivers is a DriverList, vehicles is a VehicleList and services is a
        ServiceList. drivers, vehicles and services concern the same period.
        Ensures: a DetailedServicesList object whose members are DetailedService objects
        resulting from the extension of Service objects with information of Driver and
        Vehicle objects.
        If some of the arguments is not given, it creates an empty DetailedServicesList"""

        # Creates empty DetailedServicesList
        UserList.__init__(self)

        # If some of the arguments is not give, DetailedServicesList stays empty
        if (drivers is not None) and (vehicles is not None) and (services is not None):

            services.reverse()

            driversInWaitingList = []
            waitingList = ServicesList()

            # Obtains sublist SL
            for service in services:
                driver = service.getServiceDriver()
                driverTerminated = service.getServiceDriverStatus() == Driver.STATUSTerminated
                if (driver not in driversInWaitingList) and (not driverTerminated):
                    if service.getServiceDriverStatus() == Driver.STATUSCharging:
                        service.resetVehic()
                    driversInWaitingList.append(driver)
                    waitingList.append(service)

            # Creates a list of services with further data items
            for service in waitingList:
                drivername = service.getServiceDriver()
                driver = drivers[drivername]
                vehicleplate = service.getServicePlate()
                vehicle = vehicles[vehicleplate]
                detailedService = DetailedService(driver, vehicle, service)
                self.append(detailedService)

            # Sorting according to increasing availability time,
            # untying with drivers's names

            self.sort()

    def addNoServiceDriver(self, waiting4ServicesList):
        """Adds the drivers/vehicles that had no service in the current period to the list
        of new services.

        Requires:
        waiting4ServicesList is a DetailedServicesList.
        Ensures:
        Adds the drivers that are not in self but are in waiting4ServicesList to self.
        """
        # list of names of drivers with services
        names_of_drivers_with_services = [service.getServiceDriver() for service in self]

        # services of the previous period of the drivers which got no services in this period
        ex_services_of_drivers_with_no_services = []
        for service in waiting4ServicesList:
            if service.getServiceDriver() not in names_of_drivers_with_services:
                ex_services_of_drivers_with_no_services.append(service)

        for service in ex_services_of_drivers_with_no_services:
            service.noService()
            service.resetAccumTime()
            self.append(service)

    def nextDriver(self, reservation):
        """Returns the index of the driver/vehicle to work on the reservation.

        Requires: reservation is a Reservation object.
        Ensures: an int corresponding the the position in self of the driver who's going to work
        on the reservation.

        """
        i = 0

        # checks if reservation would pass km limit of vehicle or time limit of driver and chooses another driver if that's the case
        # while cycle stops also when all the drivers were checked
        while i < len(self) and \
                (int(reservation.getReservCircuitKms()) >= self[i].calculateKmsLeft() or
                         reservation.duration() >= Driver.TIMELimit.diff(self[i].getAccumTime())):
            i += 1

        return i

    def updateServices(self, reservations):
        """Assigns drivers with their vehicles to services that were reserved.

        Requires:
        reservations is a Reservation object. objects in reservations concern a period p,
        and objects in self concern a period immediately preceding p.
        Ensures:
        a DetailedServicesList, representing the services to be provided
        in a period starting in the beginning of the period p upon they having
        been reserved as they are represented in reservations;
        Reservations with earlier booking times are served first (lexicographic
        order of clients' names is used to resolve eventual ties);
        Drivers available earlier are assigned services first (lexicographic
        order of their names is used to resolve eventual ties) under
        the following conditions:
        If a driver has less than 30 minutes left to reach their 5 hour
        daily limit of accumulated activity, he is given no further service
        in that day (this is represented with a service entry marhed with
        "terminates");
        Else if a vehicle has less than 15 kms autonomy, it is recharged
        (this is represented with a service entry marked with "charges") and
        is available 1 hour later, after recharging (this is represented with
        another service entry, marked with "standby").
        in this list L:
        drivers terminating their services earlier have priority over the ones
        terminating later;
        in case of eventual ties, drivers with less accumulated time have
        priority over the ones with more accumulated time;
        lexicographic order of drivers's names decides eventual ties
        in each case above.
        """

        waiting4ServicesList = deepcopy(self)

        new_services_list = DetailedServicesList()

        for reservation in reservations:

            # Checks if reservation would pass km limit of vehicle or time limit of driver
            # and chooses another driver if that's the case
            i = waiting4ServicesList.nextDriver(reservation)

            # If there is no driver available to a reservation, try get some to work on the next reservation
            if i == len(waiting4ServicesList):
                next
            else:

                # Creates a new service.
                service = waiting4ServicesList.pop(i)
                service.updateOneService(reservation)

                # Sets the AccumTime of service to 0 for sorting reasons.
                copy_service = deepcopy(service)
                copy_service.resetAccumTime()
                new_services_list.append(copy_service)

                # Makes driver and vehicle available again, after charging
                if service.getServiceDriverStatus() == Driver.STATUSCharging:

                    service.afterCharge()
                    waiting4ServicesList.append(deepcopy(service))

                    service.resetAccumTime()
                    new_services_list.append(service)

                elif service.getServiceDriverStatus() == Driver.STATUSStandBy:
                    waiting4ServicesList.append(deepcopy(service))

                # Sorts waiting4ServicesList so that drivers available earlier are assigned services first
                waiting4ServicesList.sort()

        # Adds to new_services_list the drivers that had no service in this period
        new_services_list.addNoServiceDriver(waiting4ServicesList)

        new_services_list.sort()

        return new_services_list

    def writeServicesFile(self, file_name, header):
        """Writes a collection of services into a file.

        Requires:
        self is a ServiceList, each Service representing the services in a period p;
        file_name is a str with the name of a .txt file whose end (before
        the .txt suffix) indicates the period p, as in the examples provided in
        the general specification (omitted here for the sake of readability);
        and header is a string with a header concerning period p, as in
        the examples provided in the general specification (omitted here for
        the sake of readability).
        Ensures:
        writing of file named file_name representing the collection of
        services in self and organized as in the examples provided in
        the general specification (omitted here for the sake of readability);
        """

        f = open(file_name + '.txt', 'w')

        h = header.split(',')

        for line in h:
            f.write(line + '\n')

        self.sort()

        for service in self:
            line = service.getServiceDriver() + ", " + service.getServicePlate() + ", " + service.getServiceClient() + ", " + \
                   str(service.getServiceDepartHour()) + ", " + str(
                    service.getServiceArrivalHour()) + ", " + service.getServiceCircuit() + ", " + \
                   service.getServiceCircuitKms() + ", " + service.getServiceDriverStatus()
            f.write(line + '\n')

        f.close()
