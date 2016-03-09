# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from constants import *
from timeTT import *
from copy import deepcopy
from ServicesList import ServicesList
from Time import Time

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

    waiting4ServicesList = deepcopy(waiting4ServicesList_prevp)

    new_services_list = ServicesList()

    for reservation in reservations_p:

        # checks if reservation would pass km limit of vehicle or time limit of driver
        # and chooses another driver if that's the case
        i = waiting4ServicesList.nextDriver(reservation)

        # if there is no driver available to a reservation, try get some to work on the next reservation
        if i == len(waiting4ServicesList):
            next
        else:

            service = waiting4ServicesList.pop(i)
            service.updateOneService(reservation)
            new_services_list.append(deepcopy(service))

            # makes driver and vehicle available again, after charging
            if service.getServiceDriverStatus() == STATUSCharging:

                service.afterCharge()
                new_services_list.append(service)
                waiting4ServicesList.append(deepcopy(service))

            elif service.getServiceDriverStatus() == STATUSStandBy:
                waiting4ServicesList.append(deepcopy(service))

            # sorts waiting4ServicesList so that drivers available earlier are assigned services first
            waiting4ServicesList.sort()

    # adds to new_services_list the drivers that had no service in this period
    new_services_list.addNoServiceDriver(waiting4ServicesList)

    return sorted(new_services_list)
