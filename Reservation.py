#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from timeTT import *


class Reservation(object):
    def __init__(self, reservClient, reservRequestedStartHour, reservRequestedEndHour, reservCircuit, reservCircuitKms):
        self._reservClient = reservClient
        self._reservRequestedStartHour = reservRequestedStartHour
        self._reservRequestedEndHour = reservRequestedEndHour
        self._reservCircuit = reservCircuit
        self._reservCircuitKms = reservCircuitKms

    def getReservClient(self):
        return self._reservClient

    def getReservRequestedStartHour(self):
        return self._reservRequestedStartHour

    def getReservRequestedEndHour(self):
        return self._reservRequestedEndHour

    def getReservCircuit(self):
        return self._reservCircuit

    def getReservCircuitKms(self):
        return self._reservCircuitKms

    def setReservClient(self, reservClient):
        self._reservClient = reservClient

    def setReservRequestedStartHour(self, reservRequestedStartHour):
        self._reservRequestedStartHour = reservRequestedStartHour

    def setReservRequestedEndHour(self, reservRequestedEndHour):
        self._reservRequestedEndHour = reservRequestedEndHour

    def setReservCircuit(self, reservCircuit):
        self._reservCircuit = reservCircuit

    def setReservCircuitKms(self, reservCircuitKms):
        self._reservCircuitKms = reservCircuitKms

    def duration(self):
        """Calculates the duration of the service requested by this reservation"""

        return diff(self.getReservRequestedEndHour(), self.getReservRequestedStartHour())

