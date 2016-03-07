# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from constants import *
from timeTT import *
from calculations import *
from copy import deepcopy
from Service import *


def addNoServiceDriver(new_services, waiting4Services):
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
    drivers_with_services = [service.getServiceDriver() for service in new_services]

    # services of the previous period of the drivers which got no services in this period
    drivers_with_no_services = []
    for service in waiting4Services:
        if service.getServiceDriver() not in drivers_with_services:
            drivers_with_no_services.append(service)

    for driver in drivers_with_no_services:
        driver.noService()
        new_services.append(driver)

    return new_services


def nextDriver(reservation, waiting4Services):
    """Returns the index of the driver/vehicle to work on the reservation.

    Requires:
    reservation is a sublist of a list with the structure as in the output of
    consultStatus.readReservationsFile; waiting4ServicesList_prevp is a list
    with the structure as in the output of consultStatus.waiting4Services.
    Ensures:
    An int corresponding to the index of waiting4Services of the driver/vehicle
    to work on the reservation. If the int returned is equal to the length
    of waiting4Services then neither of the drivers got the reservation.
    """
    i = 0
    # checks if reservation would pass km limit of vehicle or time limit of driver and chooses another driver if that's the case
    # while cycle stops also when all the drivers were checked
    while i < len(waiting4Services) and \
            (int(reservation.getReservCircuitKms()) >= waiting4Services[i].calculateKmsLeft() or
                     reservation.duration() >= diff(TIMELimit, waiting4Services[i].getAccumTime())):
        i += 1

    return i


def updateServices(reservations_p, waiting4ServicesList_prevp):
    """Assigns drivers with their vehicles to services that were reserved.

    Requires:
    reservations_p is a list with a structure as in the output of
    consultStatus.readReservationsFile; waiting4ServicesList_prevp is a list
    with the structure as in the output of consultStatus.waiting4ServicesList;
    objects in reservations_p concern a period p, and objects in
    waiting4ServicesList_prevp concern a period immediately preceding p.
    Ensures:
    list L of lists, where each list has the structure of
    consultStatus.readServicesFile, representing the services to be provided
    in a period starting in the beginning of the period p upon they having
    been reserved as they are represented in reservations_p;
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

    waiting4Services = deepcopy(waiting4ServicesList_prevp)

    new_services = []

    for reservation in reservations_p:

        # checks if reservation would pass km limit of vehicle or time limit of driver
        # and chooses another driver if that's the case
        i = nextDriver(reservation, waiting4Services)

        # if there is no driver available to a reservation, try get some to work on the next reservation
        if i == len(waiting4Services):
            next
        else:

            service = waiting4Services.pop(i)
            service.updateOneService(reservation)
            new_services.append(deepcopy(service))

            # makes driver and vehicle available again, after charging
            if service.getServiceDriverStatus() == STATUSCharging:
                # copying the object
                charged = deepcopy(service)

                charged.afterCharge()
                new_services.append(charged)
                waiting4Services.append(deepcopy(charged))

            elif service.getServiceDriverStatus() == STATUSStandBy:
                waiting4Services.append(deepcopy(service))

            # sorts waiting4Services so that drivers available earlier are assigned services first
            waiting4Services = sorted(waiting4Services)

    # adds to new_services the drivers that had no service in this period
    new_services = addNoServiceDriver(new_services, waiting4Services)

    return sorted(new_services)
