# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from constants import *
from calculations import add
from timeTT import *
from calculations import *


class Service(object):
    def __init__(self, servDriver, servPlate, servClient, servDepartHour, servArrivalHour, servCircuit, \
                 servCircuitKms, servDriverStatus):
        self._servDriver = servDriver
        self._servPlate = servPlate
        self._servClient = servClient
        self._servDepartHour = servDepartHour
        self._servArrivalHour = servArrivalHour
        self._servCircuit = servCircuit
        self._servCircuitKms = servCircuitKms
        self._servDriverStatus = servDriverStatus

    def getServiceDriver(self):
        return self._servDriver

    def getServicePlate(self):
        return self._servPlate

    def getServiceClient(self):
        return self._servClient

    def getServiceDepartHour(self):
        return self._servDepartHour

    def getServiceArrivalHour(self):
        return self._servArrivalHour

    def getServiceCircuit(self):
        return self._servCircuit

    def getServiceCircuitKms(self):
        return self._servCircuitKms

    def getServiceDriverStatus(self):
        return self._servDriverStatus

    def getAccumTime(self):
        return self._accumTime

    def getVehicleKmsDone(self):
        return self._vehicleKmsDone

    def getVehicleAutonomy(self):
        return self._vehicleAutonomy

    def setServiceDriver(self, servDriver):
        self._servDriver = servDriver

    def setServicePlate(self, servPlate):
        self._servPlate = servPlate

    def setServiceClient(self, servClient):
        self._servClient = servClient

    def setServiceDepartHour(self, servDepartHour):
        self._servDepartHour = servDepartHour

    def setServiceArrivalHour(self, servArrivalHour):
        self._servArrivalHour = servArrivalHour

    def setServiceCircuit(self, servCircuit):
        self._servCircuit = servCircuit

    def setServiceCircuitKms(self, servCircuitKms):
        self._servCircuitKms = servCircuitKms

    def setServiceDriverStatus(self, servDriverStatus):
        self._servDriverStatus = servDriverStatus

    def setAccumTime(self, AccumTime):
        self._accumTime = AccumTime

    def setVehicleAutonomy(self, vehicAutonomy):
        self._vehicleAutonomy = vehicAutonomy

    def setVehicleKmsDone(self,  kmsDone):
        self._vehicleKmsDone = kmsDone

    def setDetailedInformation(self, driver, vehicle):
        self._accumTime = driver.getDriverAccumTime()
        self._vehicleKmsDone = vehicle.getVehicleKmsDone()
        self._vehicleAutonomy = vehicle.getVehicleAutonomy()

    def resetVehic(self):
        """Changes the status of a driver/vehicle to 'standby'."""

        self.setServiceDriverStatus(STATUSStandBy)

    def afterCharge(self):
        """Updates a service to a after charge status."""

        self.setServiceClient(NOCLIENT)
        self.setServiceArrivalHour(add(self.getServiceArrivalHour(), "01:00"))
        self.setServiceDepartHour(self.getServiceArrivalHour())
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(STATUSStandBy)
        self.setVehicleKmsDone("0")

    def noService(self):
        """Update a service's list when there is no service."""

        self.setServiceClient(NOCLIENT)
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(STATUSStandBy)

    def calculateKmsLeft(self):
        """Calculates how many kilometers the vehicle of this service can still do."""

        return int(self.getVehicleAutonomy()) - int(self.getVehicleKmsDone())

    def updateOneService(self, reservation):
        """Assign a driver with her vehicle to a service that was reserved.

        Requires:
        reservation is a sublist of a list with the structure as in the output of
        consultStatus.readReservationsFile; service is a sublist of a list with
        the structure as in the output of consultStatus.waiting4ServicesList.
        Ensures:
        a list with the structure of the sublists of consultStatus.waiting4ServicesList
        where the driver and her vehicle are assigned to a reservation
        (unless the first condition of the ifelse block is true. In that case the
        structure of the list is the same as the sublists of the output of
        consultStatus.readServicesFile). See specifications of UpdateServices for more
        information.
        """
        # Adds information to the new service
        self.setServiceClient(reservation.getReservClient())

        # checks if it's going to be a delay, that is, if the driver/vehicle is not available at the requested time
        startHour, endHour = calculateDelay(self, reservation)

        self.setServiceDepartHour(startHour)
        self.setServiceArrivalHour(endHour)

        self.setServiceCircuit(reservation.getReservCircuit())
        self.setServiceCircuitKms(reservation.getReservCircuitKms())

        # Calculates how much work time is left for the driver after this service
        duration = reservation.duration()
        new_accumulated_hours = add(self.getAccumTime(), duration)
        allowed_time_left = diff(TIMELimit, new_accumulated_hours)

        # Calculates how much kms are left fot the vehicle after this service
        new_accumulated_kms = int(self.getVehicleKmsDone()) + int(self.getServiceCircuitKms())
        allowed_kms_left = int(self.getVehicleAutonomy()) - new_accumulated_kms

        # set common parameters
        self.setAccumTime(new_accumulated_hours)
        self.setVehicleKmsDone(new_accumulated_kms)

        # Adds the rest of the information, depending on the allowed time and kms left
        if allowed_time_left < TIMEThreshold:
            self.setServiceDriverStatus(STATUSTerminated)

        elif allowed_kms_left < AUTONThreshold:
            self.setServiceDriverStatus(STATUSCharging)
            self.setServiceCircuitKms(reservation.getReservCircuitKms())

        else:
            self.setServiceDriverStatus(STATUSStandBy)

        self.setVehicleAutonomy(self.getVehicleAutonomy())

    # not DRY
    def __lt__(self, other_detailedService):
        """Services with a lower _servArrivalHour are considered less than ones with a higher
        _servArrivalHour attribute. In case of equal _servArrivalHour values, the lower DetailedService
        if the one with the lower _accumTime. In the case of equal _accumTime values, the lower service
        is the one with the lower _servDriver.
        """

        # compare by arrival hour
        if self.getServiceArrivalHour() < other_detailedService.getServiceArrivalHour():
            return True
        elif self.getServiceArrivalHour() > other_detailedService.getServiceArrivalHour():
            return False
        else:

            # compare by accumulated time
            if hasattr(self, "_accumTime"):
                if self.getAccumTime() < other_detailedService.getAccumTime():
                    return True
                elif self.getAccumTime() > other_detailedService.getAccumTime():
                    return False
                else:
                    # compare by driver name
                    if self.getServiceDriver() < other_detailedService.getServiceDriver():
                        return True
                    else:
                        return False
            else:
                # compare by driver name
                if self.getServiceDriver() < other_detailedService.getServiceDriver():
                    return True
                else:
                    return False

    # detailed service information is missing
    def __str__(self):
        """String representation of the service."""

        return "Driver: " + self.getServiceDriver() + \
               "\nPlate: " + self.getServicePlate() + \
               "\nClient: " + self.getServiceClient() + \
               "\nDepartHour: " + self.getServiceDepartHour() + \
               "\nArrivalHour: " + self.getServiceArrivalHour() + \
               "\nCircuit: " + self.getServiceCircuit() + \
               "\nCircuit Kms: " + str(self.getServiceCircuitKms()) + \
               "\nDriver Status: " + self.getServiceDriverStatus()
