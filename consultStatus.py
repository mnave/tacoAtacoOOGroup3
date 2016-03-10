# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave




from constants import *
import copy
from headerRelated import removeHeader
from Service import Service
from ServicesList import ServicesList
from Time import Time
import operator


def readServicesFile(file_name):
    """Reads a file with a list of services into a collection.

    Requires:
    file_name is str with the name of a .txt file containing
    a list of services organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list L of lists, where each list corresponds to a service listed
    in file with name file_name and its elements are the elements
    belonging to that service in the order provided in the lines of
    the file.
    in this list L:
    drivers terminating their services earlier have priority over the ones
    terminating later;
    lexicographic order of drivers's names decides eventual ties
    in each case above.
    """

    inFile = removeHeader(open(file_name, "r"))

    servicesList = []
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
        servicesList.append(newService)

    servicesList = ServicesList(servicesList)

    return servicesList


def waiting4ServicesList(drivers_p, vehicles_p, services_p):
    """Organizes a list of active drivers with their assigned
    vehicles that can take further services.

    Requires:
    drivers_p is a dict with a structure as in the output
    of readDriversFile; vehicles_p is a dict with the structure as in
    the output of readVehiclesFile; services_p is a list with the structure
    as in the output of readServicesFile; the objects in drivers_p,
    vehicles_p and services_p concern the same period p.
    Ensures:
    a list L of lists with a structure similar to the output of
    readServicesFile and obtained by:
    extracting the sublist SL of services_p where each list in
    that sublist SL corresponds to the last representation of an active
    driver, converted to a “standby” status (older representations of active
    drivers and representations of terminated drivers are excluded),
    and by appending to each list of that subset SL 3 further elements:
    one with the accumulated time of the driver, another with the autonomy
    of his vehicle in kilometers for a fully charged batery, and yet
    another with the accumulated kilometers of that vehicle;
    in this list L:
    drivers terminating their services earlier have priority over the ones
    terminating later;
    in case of eventual ties, drivers with less accumulated time have
    priority over the ones with more accumulated time;
    lexicographic order of drivers's names decides eventual ties
    in each case above.
    """

    serviceList = copy.deepcopy(services_p)
    serviceList.reverse()

    driversInWaitingList = []
    detailedWaitingList = ServicesList()

    # Obtains sublist SL
    for service in serviceList:
        driver = service.getServiceDriver()
        driverTerminated = service.getServiceDriverStatus() == STATUSTerminated
        if (driver not in driversInWaitingList) and (not driverTerminated):
            if service.getServiceDriverStatus() == STATUSCharging:
                service.resetVehic()
            driversInWaitingList.append(driver)
            detailedWaitingList.append(service)

    # Creates a list of services with further data items
    for service in detailedWaitingList:
        drivername = service.getServiceDriver()
        driver = drivers_p[drivername]
        vehicleplate = service.getServicePlate()
        vehicle = vehicles_p[vehicleplate]
        service.setDetailedInformation(driver, vehicle)

    # Sorting according to increasing availability time,
    # untying with drivers's names

    detailedWaitingList.sort()

    return detailedWaitingList


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
