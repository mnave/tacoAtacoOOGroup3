#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


import constants
import copy
import timeTT
from operator import itemgetter
import Driver
import Vehicle
import Reservation
import Service



def removeHeader(file):
    return file.readlines()[constants.NUMBEROfLinesInHeader:]


def getHeader(file):
    return file.readlines()[:constants.NUMBEROfLinesInHeader]


def readDriversFile(file_name):
    """Reads a file with a list of drivers into a collection.

    Requires:
    file_name is str with the name of a .txt file containing
    a list of drivers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    dict where each item corresponds to a driver listed in
    file with name file_name, a key is the string with the name of a driver,
    and a value is the list with the other elements belonging to that
    driver, in the order provided in the lines of the file.
    """

    inFile = removeHeader(open(file_name, "r"))
    driversDict = {}
    for line in inFile:
        driverData = line.rstrip().split(", ")
        driverName = driverData[constants.INDEXDriverName]
        driverEntryHour = driverData[constants.INDEXStartingHour]
        driverAccumTime = driverData[constants.INDEXWorkingHours]
        newDriver = Driver(driverName, driverEntryHour, driverAccumTime)
        driversDict[driverName] = newDriver

    return driversDict


def readVehiclesFile(file_name):
    """
    Reads a file with a list of vehicles into a collection.
    Requires:
    file_name is str with the name of a .txt file containing
    a list of vehicles organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    dict where each item corresponds to a driver listed in
    file with name file_name, a key is the string with the plate of a vehicle,
    and a value is the list with the other elements belonging to that
    plate, in the order provided in the lines of the file.
    """

    inFile = removeHeader(open(file_name, "r"))

    vehiclesDict = {}
    for line in inFile:
        vehicleData = line.rstrip().split(", ")
        vehiclePlate = vehicleData[constants.INDEXVehiclePlateInDict]
        vehicleModel = vehicleData[constants.INDEXVehicleModel]
        vehicleAutonomy = vehicleData[constants.INDEXVehicleAutonomyInDict]
        vehicleKms = vehicleData[constants.INDEXVehicleAccumulatedKms]
        newVehicle = Vehicle(vehiclePlate, vehicleModel, vehicleAutonomy, vehicleKms)
        vehiclesDict[vehiclePlate] = newVehicle

    return vehiclesDict



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
        servDriver = servData[constants.INDEXDriverName]
        servPlate = servData[constants.INDEXVehiclePlate]
        servClient = servData[constants.INDEXClientName]
        servDeparHour = servData[constants.INDEXDepartureHour]
        servArrivalHour = servData[constants.INDEXArrivalHour]
        servCircuit = servData[constants.INDEXCircuitId]
        servCircuitKms = servData[constants.INDEXCircuitKms]
        servDriverStatus = servData[constants.INDEXDriverStatus]
        newService = Service(servDriver, servPlate, servClient, servDeparHour, servArrivalHour, \
                              servCircuit, servCircuitKms, servDriverStatus)
        servicesList.append(newService)

    return servicesList


def readReservationsFile(file_name):
    """Reads a file with a list of reservations into a collection.

    Requires:
    file_name is a string with the name of a .txt file containing
    a list of reservations organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list L of lists, where each list corresponds to a reservation
    listed in file name with file_name and its elements are
    the elements belonging to that reservation in the order provided in
    the lines of the file.
    in this list L:
    clients reserving a service with an earlier starting time have
    priority over the ones with later starting times;
    lexicographic order of clients's names decides eventual ties.
    """

    inFile = removeHeader(open(file_name, "r"))
    reservationsList = []

    for line in inFile:
        reservData = line.rstrip().split(", ")
        reservClient = reservData[constants.INDEXClientNameInReservation]
        reservRequestedStartHour = reservData[constants.INDEXRequestedStartHour]
        reservRequestedEndHour = reservData[constants.INDEXRequestedEndHour]
        reservCircuit = reservData[constants.INDEXCircuitInReservation]
        reservCircuitKms = reservData[constants.INDEXCircuitKmsInReservation]
        newReserv = Reservation(reservClient, reservRequestedStartHour, reservRequestedEndHour, reservCircuit,
                                 reservCircuitKms)
        reservationsList.append(newReserv)

    return reservationsList

#not seen so far:
def resetVehic(service_p):
    """ Resets the vehicle after charging.

    Requires:
    services_p is a list of services where p stands for the working period
    Ensures:
    an updated List with the reset of driver/vehicle details after charging
    (eg: _no_client_| _no_circuit_| accumulated Kms = 0)
    """

    serv = copy.deepcopy(service_p)
    serv[constants.INDEXArrivalHour] = timeTT.add(serv[constants.INDEXArrivalHour], constants.RECHDURATION)
    serv[constants.INDEXDepartureHour] = serv[constants.INDEXArrivalHour]
    serv[constants.INDEXClientName] = constants.NOCLIENT
    serv[constants.INDEXCircuitId] = constants.NOCIRCUIT
    serv[constants.INDEXCircuitKms] = '0'
    serv[constants.INDEXDriverStatus] = constants.STATUSStandBy
    return serv


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
    detailedWaitingList = []

    # Obtains sublist SL
    for service in serviceList:
        driver = service[constants.INDEXDriverName]
        driverTerminated = service[constants.INDEXDriverStatus] == constants.STATUSTerminated
        if (driver not in driversInWaitingList) and (not driverTerminated):
            # DEPRECATED: service = resetVehic(service, mode="standby")
            if service[constants.INDEXDriverStatus] == constants.STATUSCharging:  # REPLACEMENT
                service = resetVehic(service)  # REPLACEMENT
            driversInWaitingList.append(driver)
            detailedWaitingList.append(service)

    # Enriches SL with 3 further data items
    for service in detailedWaitingList:
        driverName = service[constants.INDEXDriverName]
        driverAccumulatedTime = drivers_p[driverName][constants.INDEXAccumulatedTimeInDict]
        service.append(driverAccumulatedTime)
        vehiclePlate = service[constants.INDEXVehiclePlate]
        vehicleKms = vehicles_p[vehiclePlate][constants.INDEXVehicleAutonomyInDict:]
        service.extend(vehicleKms)

    # Puts it back to the original order
    detailedWaitingList.reverse()

    # Sorting according to increasing availability time,
    # untying with drivers's names
    detailedWaitingList = sorted(detailedWaitingList,
                                 key=itemgetter(constants.INDEXArrivalHour,
                                                constants.INDEXAccumulatedTime,
                                                constants.INDEXDriverName))

    return detailedWaitingList
