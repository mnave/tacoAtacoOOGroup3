# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


class Reservation(object):
    """ A Taco-a-Taco Reservation"""

    def __init__(self, reservClient, reservRequestedStartHour, reservRequestedEndHour, reservCircuit, reservCircuitKms):
        """Creates a new Reservation object.

        Requires: reservClient is a string representing the name of the client. reservRequestedStartHour
        and reservRequestedEndHour Time objects representing the requested times for the beginning and end,
        respectively,  of the reservation. reservCircuit is a string with the circuit reserved and
        reservCircuitKms is a string with the Kms of the reserved circuit.
        Ensures: Creation of a new Reservation object."""

        self._reservClient = reservClient
        self._reservRequestedStartHour = reservRequestedStartHour
        self._reservRequestedEndHour = reservRequestedEndHour
        self._reservCircuit = reservCircuit
        self._reservCircuitKms = reservCircuitKms

    def getReservClient(self):
        """Name of the client requesting the service."""

        return self._reservClient

    def getReservRequestedStartHour(self):
        """The requested start hour of the service."""

        return self._reservRequestedStartHour

    def getReservRequestedEndHour(self):
        """The requested end hour of the service."""

        return self._reservRequestedEndHour

    def getReservCircuit(self):
        """The requested circuit name."""

        return self._reservCircuit

    def getReservCircuitKms(self):
        """The distance, in kms of the requested circuit."""

        return self._reservCircuitKms

    def setReservClient(self, reservClient):
        """Sets the name of the client of the reservation.

        Requires: reservClient is a str representing the client name.
        Ensures: self.getReservClient() == reservClient  """

        self._reservClient = reservClient

    def setReservRequestedStartHour(self, reservRequestedStartHour):
        """Sets the requested start hour of the reservation.

        Requires: reservRequestedStartHour is a Time object representing the requested start hour of the service.
        Ensures: self.getReservRequestedStartHour() == reservRequestedStartHour  """

        self._reservRequestedStartHour = reservRequestedStartHour

    def setReservRequestedEndHour(self, reservRequestedEndHour):
        """Sets the requested end hour of the reservation.

        Requires: reservRequestedEndHour is a Time object representing the requested end hour of the service.
        Ensures: self.getReservRequestedEndHour() == reservRequestedEndHour"""

        self._reservRequestedEndHour = reservRequestedEndHour

    def setReservCircuit(self, reservCircuit):
        """Sets the requested circuit name of the reservation.

        Requires: reservCircuit is a str representing the name of the circuit.
        Ensures: self.getReservCircuit() == reservCircuit  """

        self._reservCircuit = reservCircuit

    def setReservCircuitKms(self, reservCircuitKms):
        """Sets the distance, in kms, of the requested circuit of the reservation.

        Requires: reservCircuitKms is a str representing the distance of the circuit, in kilometers.
        Ensures: self.getReservCircuitKms(() == reservCircuitKms"""

        self._reservCircuitKms = reservCircuitKms

    def duration(self):
        """Calculates the duration of the service requested by this reservation"""

        return self.getReservRequestedEndHour().diff(self.getReservRequestedStartHour())

    def __str__(self):
        """String representation of the reservation"""

        return "Client name:" + self.getReservClient() + "\n" + \
               "Requested Start Hour: " + self.getReservRequestedStartHour() + "\n" + \
               "Requested End Hour: " + self.getReservRequestedEndHour() + "\n" + \
               "Circuit name: " + self.getReservCircuit() + "\n" + \
               "Distance (in kms): " + self.getReservCircuitKms()
