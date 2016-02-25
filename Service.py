#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from constants import *
from calculations import add

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

    def resetVehic(self):
        """Changes the status of a driver/vehicle to 'standby'."""

        self.setServiceDriverStatus(STATUSStandBy)

    def afterCharge(self):
        """Updates a service to a after charge status."""

        self.setServiceDriver(NOCLIENT)
        self.setServiceArrivalHour(add(self.getServiceArrivalHour(), "01:00"))
        self.setServiceDepartHour(self.getServiceArrivalHour())
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(STATUSStandBy)

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
