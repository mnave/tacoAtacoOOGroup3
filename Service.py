#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


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
