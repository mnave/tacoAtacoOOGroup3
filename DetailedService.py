#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from Service import Service
from Time import Time
from constants import *


class DetailedService(Service):
    def __init__(self, driver, vehicle, service):
        Service.__init__(self, service.getServiceDriver(), service.getServicePlate(), service.getServiceClient(), \
                         service.getServiceDepartHour(), service.getServiceArrivalHour(), service.getServiceCircuit(), \
                         service.getServiceCircuitKms(), service.getServiceDriverStatus())
        self._accumTime = driver.getDriverAccumTime()
        self._vehicleKmsDone = vehicle.getVehicleKmsDone()
        self._vehicleAutonomy = vehicle.getVehicleAutonomy()

    def getAccumTime(self):
        return self._accumTime

    def getVehicleKmsDone(self):
        return self._vehicleKmsDone

    def getVehicleAutonomy(self):
        return self._vehicleAutonomy

    def setAccumTime(self, AccumTime):
        self._accumTime = AccumTime

    def setVehicleAutonomy(self, vehicAutonomy):
        self._vehicleAutonomy = vehicAutonomy

    def setVehicleKmsDone(self,  kmsDone):
        self._vehicleKmsDone = kmsDone

    def afterCharge(self):
        """Updates a service to a after charge status."""

        self.setServiceClient(NOCLIENT)
        self.setServiceArrivalHour(self.getServiceArrivalHour().add(Time("01:00")))
        self.setServiceDepartHour(self.getServiceArrivalHour())
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(STATUSStandBy)
        self.setVehicleKmsDone("0")

    def updateOneService(self, reservation):
        """Assign a driver with her vehicle to a service that was reserved.

        Requires:
        reservation is a Reservation object.
        Ensures:
        self attributes get updated considering the new reservation.
        """
        # Adds information to the new service
        self.setServiceClient(reservation.getReservClient())

        # checks if it's going to be a delay, that is, if the driver/vehicle is not available at the requested time
        self.calculateNewStartAndEndHour(reservation)

        self.setServiceCircuit(reservation.getReservCircuit())
        self.setServiceCircuitKms(reservation.getReservCircuitKms())

        # Calculates how much work time is left for the driver after this service
        duration = reservation.duration()
        new_accumulated_hours = self.getAccumTime().add(duration)
        allowed_time_left = Time(TIMELimit).diff(new_accumulated_hours)

        # Calculates how much kms are left fot the vehicle after this service
        new_accumulated_kms = int(self.getVehicleKmsDone()) + int(self.getServiceCircuitKms())
        allowed_kms_left = int(self.getVehicleAutonomy()) - new_accumulated_kms

        # set common parameters
        self.setAccumTime(new_accumulated_hours)
        self.setVehicleKmsDone(new_accumulated_kms)

        # Adds the rest of the information, depending on the allowed time and kms left
        if allowed_time_left < Time(TIMEThreshold):
            self.setServiceDriverStatus(STATUSTerminated)

        elif allowed_kms_left < AUTONThreshold:
            self.setServiceDriverStatus(STATUSCharging)
            self.setServiceCircuitKms(reservation.getReservCircuitKms())

        else:
            self.setServiceDriverStatus(STATUSStandBy)

        self.setVehicleAutonomy(self.getVehicleAutonomy())


    def calculateKmsLeft(self):
        """Calculates how many kilometers the vehicle of this service can still do."""

        return int(self.getVehicleAutonomy()) - int(self.getVehicleKmsDone())

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

    def __str__(self):
        return Service.__str__(self) + \
            "\nAccum Time: " + self._accumTime + \
            "\nvehiclePlate: " + self._vehiclePlate + \
            "\nvehicleKmsLeft: " + self._vehicleKmsLeft + \
            "\nvehicleAutonomy: " + self._vehicleAutonomy


