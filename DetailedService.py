# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from Service import Service
from Driver import Driver
from Time import Time
from constants import *


class DetailedService(Service):
    """A DetailedService. Similar to Service but with more attributes and methods"""

    def __init__(self, driver, vehicle, service):
        """Creates a DetailedService object, subclass of Service.

        Requires: driver is a Driver object, vehicle is a Vehicle object and service is a Service object.
        Ensures: a DetailedService object - a Service object enriched with three
        attributes: drivers' accumulated time and vehicles' Autonomy and Kms done.
        """

        Service.__init__(self, service.getServiceDriver(), service.getServicePlate(), service.getServiceClient(), \
                         service.getServiceDepartHour(), service.getServiceArrivalHour(), service.getServiceCircuit(), \
                         service.getServiceCircuitKms(), service.getServiceDriverStatus())
        self._accumTime = driver.getDriverAccumTime()
        self._vehicleKmsDone = vehicle.getVehicleKmsDone()
        self._vehicleAutonomy = vehicle.getVehicleAutonomy()

    def getAccumTime(self):
        """The driver's accumulated time since the beggining of the working day. """

        return self._accumTime

    def getVehicleKmsDone(self):
        """The distance (in kms) traveled by the vehicle since the last time it was charged. """

        return self._vehicleKmsDone

    def getVehicleAutonomy(self):
        """The autonomy (in kms) of the vehicle. """

        return self._vehicleAutonomy

    def setAccumTime(self, AccumTime):
        """Sets the driver's accumulated time since the beggining of the working day.

        Requires: AccumTime
        Ensures: self.getAccumTime() == AccumTime"""

        self._accumTime = AccumTime

    def setVehicleAutonomy(self, vehicAutonomy):
        """Sets the distance (in kms) traveled by the vehicle since the last time it was charged.

        Requires: vehicAutonomy
        Ensures: self.getVehicleKmsDone() == vehicAutonomy"""

        self._vehicleAutonomy = vehicAutonomy

    def setVehicleKmsDone(self, kmsDone):
        """Sets the autonomy (in kms) of the vehicle.

        Requires: kmsDone
        Ensures: self.getVehicleAutonomy() == kmsDone"""

        self._vehicleKmsDone = kmsDone

    def resetAccumTime(self):
        """Sets the accumlated time of the driver to 0.

        Ensures: self.setAccumTime() = 0"""

        self._accumTime = 0

    def afterCharge(self):
        """Updates a service to a after charge status."""

        self.setServiceClient(NOCLIENT)
        self.setServiceArrivalHour(self.getServiceArrivalHour().add(Time("01:00")))
        self.setServiceDepartHour(self.getServiceArrivalHour())
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(Driver.STATUSStandBy)
        self.setVehicleKmsDone("0")

    def updateOneService(self, reservation):
        """Assign a driver and his vehicle to a service that was reserved.

        Requires:
        reservation is a Reservation object.
        Ensures:
        self attributes get updated considering the new reservation.
        """
        # Adds information to the new service
        self.setServiceClient(reservation.getReservClient())

        # checks if it's going to be a delay, that is, if the driver/vehicle is not available at the requested time
        self.calculateDepartAndArrivalHour(reservation)

        self.setServiceCircuit(reservation.getReservCircuit())
        self.setServiceCircuitKms(reservation.getReservCircuitKms())

        # Calculates how much work time is left for the driver after this service
        duration = reservation.duration()
        new_accumulated_hours = self.getAccumTime().add(duration)
        allowed_time_left = Driver.TIMELimit.diff(new_accumulated_hours)

        # Calculates how much kms are left fot the vehicle after this service
        new_accumulated_kms = int(self.getVehicleKmsDone()) + int(self.getServiceCircuitKms())
        allowed_kms_left = int(self.getVehicleAutonomy()) - new_accumulated_kms

        # set common parameters
        self.setAccumTime(new_accumulated_hours)
        self.setVehicleKmsDone(new_accumulated_kms)

        # Adds the rest of the information, depending on the allowed time and kms left
        if allowed_time_left < Driver.TIMEThreshold:
            self.setServiceDriverStatus(Driver.STATUSTerminated)

        elif allowed_kms_left < AUTONThreshold:
            self.setServiceDriverStatus(Driver.STATUSCharging)
            self.setServiceCircuitKms(reservation.getReservCircuitKms())

        else:
            self.setServiceDriverStatus(Driver.STATUSStandBy)

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
        elif self.getServiceArrivalHour() == other_detailedService.getServiceArrivalHour():

            # compare by accumulated time
            if self.getAccumTime() < other_detailedService.getAccumTime():
                return True
            elif self.getAccumTime() == other_detailedService.getAccumTime():

                # compare by driver name
                if self.getServiceDriver() < other_detailedService.getServiceDriver():
                    return True

        return False

    def __eq__(self, other_DetailedService):
        pass

    def __str__(self):
        """A str representation of a DetailedService"""

        return Service.__str__(self) + \
               "\nAccum Time: " + self._accumTime + \
               "\nvehiclePlate: " + self._vehiclePlate + \
               "\nvehicleKmsLeft: " + self._vehicleKmsLeft + \
               "\nvehicleAutonomy: " + self._vehicleAutonomy
