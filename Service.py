# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from constants import *
from Time import Time
from Driver import Driver


class Service(object):
    """A Taca-a-Taco service"""

    def __init__(self, servDriver, servPlate, servClient, servDepartHour, servArrivalHour, servCircuit, \
                 servCircuitKms, servDriverStatus):

        """Creates a new Service object.

        Requires: servDriver is a srt representing name of a driver. ServPlate is a str representing the plate
        of a vehicle. servClient is a str representing the client's name. servDepartHour is a str in the "HH:MM" format
        representing the departing hour of the service. servArrivalHour is a str in the "HH:MM" format
        representing the arrival hour of the service. servCircuit is a str representing the name of the circuit done by
        the service. servCircuitKms is a str representing the number of kilometers done in the service. servDriverStatus
        is a str representing the drivers status. Check the general specification for more information."""

        self._servDriver = servDriver
        self._servPlate = servPlate
        self._servClient = servClient
        self._servDepartHour = servDepartHour
        self._servArrivalHour = servArrivalHour
        self._servCircuit = servCircuit
        self._servCircuitKms = servCircuitKms
        self._servDriverStatus = servDriverStatus

    def getServiceDriver(self):
        """Name of the service driver."""

        return self._servDriver

    def getServicePlate(self):
        """Plate of the service vehicle."""

        return self._servPlate

    def getServiceClient(self):
        """Name of the service client."""

        return self._servClient

    def getServiceDepartHour(self):
        """Service departing hour."""

        return self._servDepartHour

    def getServiceArrivalHour(self):
        """Service arrival hour."""

        return self._servArrivalHour

    def getServiceCircuit(self):
        """Name of the service circuit."""

        return self._servCircuit

    def getServiceCircuitKms(self):
        """Distance of the service, in kilometers."""

        return self._servCircuitKms

    def getServiceDriverStatus(self):
        """Status of the driver."""

        return self._servDriverStatus

    def setServiceDriver(self, servDriver):
        """Set the name of the service driver.

        Requires: servDriver is a srt representing name of a driver.
        Ensures: self.getServiceDriver() == servDriver
        """

        self._servDriver = servDriver

    def setServicePlate(self, servPlate):
        """Set the plate of the service vehicle.

        Requires: servPlate is a str reprensenting the vehicle's plate.
        Ensures: self.getServicePlate() == servPlate
        """

        self._servPlate = servPlate

    def setServiceClient(self, servClient):
        """Set the name of the service client.

        Requires: servClient is a str representing the client name.
        Ensures: self.getServiceClient() == servClient
        """

        self._servClient = servClient

    def setServiceDepartHour(self, servDepartHour):
        """Set the service departing hour.

        Requires: servDepartHour is a str in the format "HH:MM" representing the departing hour of the service.
        Ensures: self.getServiceDepartHour() == servDepartHour
        """

        self._servDepartHour = servDepartHour

    def setServiceArrivalHour(self, servArrivalHour):
        """Set the service arrival hour.

        Requires: servArrivalHour is a str in the format "HH:MM" representing the arrival hour of the service.
        Ensures: self.getServiceArrivalHour(() == servArrivalHour
        """

        self._servArrivalHour = servArrivalHour

    def setServiceCircuit(self, servCircuit):
        """Set the name of the service circuit.

        Requires: servCircuit is a str representing the circuit name.
        Ensures: self.getServiceCircuit() == servCircuit
        """

        self._servCircuit = servCircuit

    def setServiceCircuitKms(self, servCircuitKms):
        """Set the distance of the service, in kilometers.

        Requires: servCircuitKms is a str representing the distance of the circuit, in kilometers.
        Ensures: self.getServiceCircuitKms() == servCircuitKms
        """

        self._servCircuitKms = servCircuitKms

    def setServiceDriverStatus(self, servDriverStatus):
        """Set the status of the driver.

        Requires: servDriverStatus is str representing the status of the driver.
        Ensures: self.getServiceDriverStatus() == servDriverStatus
        """

        self._servDriverStatus = servDriverStatus

    def resetVehic(self):
        """Changes the status of a driver/vehicle to 'standby'."""

        self.setServiceDriverStatus(STATUSStandBy)

    def noService(self):
        """Update a service's list when there is no service."""

        self.setServiceClient(NOCLIENT)
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(Driver.STATUSStandBy)

    def calculateDepartAndArrivalHour(self, reservation):
        """Calculates the Service departing and arrival hour considering the new reservation.

        Requires:
        reservation is a Reservation object.
        Ensures:
        self depart and arrival hour get changed considering the new reservation.
        """
        # default delay if no delay
        delay = Time('00:00')

        # if the driver only arrives from the previous service after the client requested hour,
        # calculate delay.
        if self.getServiceArrivalHour().diff(reservation.getReservRequestedStartHour()) > Time('00:00'):
            delay = self.getServiceArrivalHour().diff(reservation.getReservRequestedStartHour())

        # calculates the depart and arrival hour of the new service, considering the possible delay.
        departHour = reservation.getReservRequestedStartHour().add(delay)
        arrivalHour = reservation.getReservRequestedEndHour().add(delay)

        self.setServiceDepartHour(departHour)
        self.setServiceArrivalHour(arrivalHour)

    def __lt__(self, other_Service):
        """Services with a lower _servArrivalHour are considered less than ones with a higher
        _servArrivalHour attribute. In case of equal _servArrivalHour values, the lower DetailedService
        if the one with the lower _accumTime. In the case of equal _accumTime values, the lower service
        is the one with the lower _servDriver.
        """

        # Compare by arrival hour.
        if self.getServiceArrivalHour() < other_Service.getServiceArrivalHour():
            return True
        elif self.getServiceArrivalHour() == other_Service.getServiceArrivalHour():

            # Compare by Driver name.
            if self.getServiceDriver() < other_Service.getServiceDriver():
                return True

        return False

    def __eq__(self, other_Service):
        pass

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
