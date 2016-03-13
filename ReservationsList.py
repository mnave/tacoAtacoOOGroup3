# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from UserList import UserList
from headerRelated import removeHeader
from constants import *
from Time import Time
from Reservation import Reservation


class ReservationsList(UserList):
    """ Collection of Reservations.
    UserList works as wrapper for list objects, allowing to manipulate ReservationsList
    object with all the built-in list methods.
    """

    def __init__(self, file_name=None):
        """Creates a ReservationList composed by Reservation objects, from a file with a list of reservations.

        Requires: If given, file_name is str with the name of a .txt file containing
        a list of reservations organized as in the examples provided in
        the general specification (omitted here for the sake of readability).

        Ensures:
        if file_name is given:
                a ReservationList, composed by objects of class Service that correspond to the services listed
                in file with name file_name.
        if file_name is none:
                a empty ServiceList."""

        UserList.__init__(self)

        if file_name is not None:
            inFile = removeHeader(open(file_name, "r"))

            for line in inFile:
                reservData = line.rstrip().split(", ")
                reservClient = reservData[INDEXClientNameInReservation]
                reservRequestedStartTime = Time(reservData[INDEXRequestedStartHour])
                reservRequestedEndTime = Time(reservData[INDEXRequestedEndHour])
                reservCircuit = reservData[INDEXCircuitInReservation]
                reservCircuitKms = reservData[INDEXCircuitKmsInReservation]
                newReserv = Reservation(reservClient, reservRequestedStartTime, reservRequestedEndTime, reservCircuit,
                                        reservCircuitKms)
                self.append(newReserv)

    def __str__(self):
        '''
        str method for printing purposes
        '''

        output = ""

        for reservation in self:
            output += reservation.getReservClient() + '\n'

        return output
