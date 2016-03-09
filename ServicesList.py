from UserList import UserList
from Time import Time
from constants import *


class ServicesList(UserList):

    def __init__(self, list=None):
        if list is None:
            UserList.__init__(self)
        else:
            UserList.__init__(self, list)

    def addNoServiceDriver(self, waiting4ServicesList):
        """Adds the drivers/vehicles that had no service in the current period to the list
        of new services.

        Requires:
        new_services is a list of lists with the structure of the output of
        consultStatus.readServicesFile although not necessarily ordered;
        waiting4Services is a list of lists with the structure of
        consultStatus.waiting4ServicesList
        Ensures:
        a list of lists similar to new_services but with list(s), corresponding
        to drivers/vehicles which had no service in the current, appended to it.
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
            self.append(service)

    def nextDriver(self, reservation):
        """Returns the index of the driver/vehicle to work on the reservation.

        Requires:
        reservation is a Reservation object.
        self is a ServiceList object containing Services with the detailed attributes defined.
        Ensures:

        """
        i = 0

        # checks if reservation would pass km limit of vehicle or time limit of driver and chooses another driver if that's the case
        # while cycle stops also when all the drivers were checked
        while i < len(self) and \
                (int(reservation.getReservCircuitKms()) >= self[i].calculateKmsLeft() or
                         reservation.duration() >= Time(TIMELimit).diff(self[i].getAccumTime())):
            i += 1

        return i


