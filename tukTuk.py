# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

import sys
from planning import updateServices
from headerRelated import createNewHeader, getHeader
from timeTT import changeFormatTime, getPreviousPeriod
from consultStatus import *
from DriversDict import DriversDict
from VehiclesDict import VehiclesDict
from ReservationsList import ReservationsList
from ServicesList import ServicesList
from DetailedServicesList import DetailedServicesList

nextPeriod = sys.argv[1]
driversFileName = sys.argv[2]
vehiclesFileName = sys.argv[3]
servicesFileName = sys.argv[4]
reservationsFileName = sys.argv[5]


def checkPreConditions(nextPeriod, driversFileName, vehiclesFileName,
                       servicesFileName, reservationsFileName):
    """Checks the preconditions.
    Requires:
    The same as update (ommitted here to avoid redudancy)
    Ensures:
    returns bool value False if some of the conditions are not met
    and True otherwise
    """

    headerDrivers = getHeader(driversFileName)
    headerVehicles = getHeader(vehiclesFileName)
    headerServices = getHeader(servicesFileName)
    headerReservations = getHeader(reservationsFileName)

    previousPeriod = getPreviousPeriod(nextPeriod)

    # Changes the format of the period to the one in the header of files
    nextPeriodOther = changeFormatTime(nextPeriod)
    previousPeriodOther = changeFormatTime(previousPeriod)

    # NextPeriod is a str from the set 0911, 1113, ..., 1921
    if nextPeriod not in ['0911', '1113', '1315', '1517', '1719', '1921']:
        return False

    # The files whose names are driversFileName, vehiclesFileName, servicesFileName and reservationsFileName
    # concern the same company and the same day;
    elif not (headerDrivers[INDEXCompany:INDEXDate + 1] == headerVehicles[INDEXCompany:INDEXDate + 1] ==
                  headerServices[INDEXCompany:INDEXDate + 1] == headerReservations[INDEXCompany:INDEXDate + 1]):
        return False

    # The file whose name is reservationsFileName concerns the period indicated by nextPeriod
    elif headerReservations[INDEXPeriod].strip() != nextPeriodOther:
        return False

    # The files whose names are driversFileName, vehiclesFileName, servicesFileName concern the period
    # immediately preceding the period indicated by nextPeriod;

    elif not (headerDrivers[INDEXPeriod].strip() == headerVehicles[INDEXPeriod].strip() ==
                  headerServices[INDEXPeriod].strip() == previousPeriodOther):
        return False

    # The file name reservationsFileName ends (before the .txt extension) with
    # the string nextPeriod;
    elif reservationsFileName[-8:-4] != nextPeriod:
        return False

    # The file names driversFileName, vehiclesFileName and servicesFileName
    # end (before their .txt extension) with the string representing
    # the period immediately preceding the one indicated by nextPeriod,
    # from the set 0709, 0911, ..., 1719;
    elif not (driversFileName[-8:-4] == vehiclesFileName[-8:-4] == servicesFileName[-8:-4] == previousPeriod):
        return False

    else:
        return True


def update(nextPeriod, driversFileName, vehiclesFileName,
           servicesFileName, reservationsFileName):
    """Obtains the planning for a period of activity.
    Requires:
    nextPeriod is a str from the set 0911, 1113, ..., 1921 indicating the
    2 hour period to be planned;
    driversFileName is a str with the name of a .txt file containing a list
    of drivers organized as in the examples provided;
    vehiclesFileName is a str with the name of a .txt file containing a list
    of vehicles organized as in the examples provided;
    servicesFileName is a str with the name of a .txt file containing a list
    of services organized as in the examples provided;
    reservationsFileName is a str with the name of a .txt file containing
    a list of reserved services organized as in the examples provided;
    the files whose names are driversFileName, vehiclesFileName,
    servicesFileName and reservationsFileName concern the same company and
    the same day;
    the file whose name is reservationsFileName concerns the period
    indicated by nextPeriod;
    the files whose names are driversFileName, vehiclesFileName,
    servicesFileName concern the period immediately preceding the period
    indicated by nextPeriod;
    the file name reservationsFileName ends (before the .txt extension) with
    the string nextPeriod;
    the file names driversFileName, vehiclesFileName and servicesFileName
    end (before their .txt extension) with the string representing
    the period immediately preceding the one indicated by nextPeriod,
    from the set 0709, 0911, ..., 1719;
    Ensures:
    writing of .txt file containing the updated list of services for
    the period nextPeriod according to the requirements in the general
    specifications provided (omitted here for the sake of readability);
    the name of that file is outputXXYY.txt where XXYY represents
    the nextPeriod.
    """

    if checkPreConditions(nextPeriod, driversFileName, vehiclesFileName, servicesFileName, reservationsFileName):

        file_name = "output" + nextPeriod

        header = createNewHeader(servicesFileName, nextPeriod)

        drivers = DriversDict(driversFileName)
        vehicles = VehiclesDict(vehiclesFileName)
        services = ServicesList(servicesFileName)
        reservations = ReservationsList(reservationsFileName)

        # 1st period
        if nextPeriod == "0911" and ("0911" in reservationsFileName):
            empty_services = emptyServices(drivers, vehicles)
            waiting4services = DetailedServicesList(drivers, vehicles, empty_services)
        else:
            waiting4services = DetailedServicesList(drivers, vehicles, services)

        new_services = updateServices(reservations, waiting4services)

        new_services.writeServicesFile(file_name, header)

    else:
        raise IOError('File names and/or headers not consistent.')


update(nextPeriod, driversFileName, vehiclesFileName, servicesFileName, reservationsFileName)
