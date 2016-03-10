# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from constants import *
import copy
from headerRelated import removeHeader
from Service import Service
from DetailedService import DetailedService
from ServicesList import ServicesList
from Time import Time
import operator


def emptyServices(drivers, vehicles):
    """
    Requires: drivers is a dict with a structure as in the output
    of readDriversFile; vehicles is a dict with the structure as in
    the output of readVehiclesFile.
    Ensures: A list of services regarding the first working period (0911);
    vehicles, lexicographic sorted by plate, are attributed to drivers
    according to their entry hour. All the service-related information is
    set as a "no service" (_no_client_, _no_circuit_, service kms = 0), Arrival and Departure
    hours are set as the Driver's entry hour and being ready to work,
    drivers' status is standby, of course!
    """

    lstDrivers = []
    lstVehicles = []
    lstService = ServicesList()
    for i in drivers.values():
        lstDrivers.append(i)

    for j in vehicles.values():
        lstVehicles.append(j._plate)

    # sort drivers for the 1st period: 0911
    d = sorted(lstDrivers, key=operator.attrgetter("_entryHour"))
    v = sorted(lstVehicles)

    for i in range(len(d)):
        driverName = d[i].getDriverName()
        vehiclePlate = v[i]
        drv = d[i]
        serv = Service(driverName, vehiclePlate, "", drv.getDriverEntryHour(), drv.getDriverEntryHour(), "", "", "")
        serv.noService()
        lstService.append(serv)
    return lstService
