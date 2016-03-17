# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from UserList import UserList
from TimeTT import Time
from Reservation import Reservation
from FileUtil import *


class ReservationsList(UserList):
    """ Collection of Reservations.
    UserList works as wrapper for list objects, allowing to manipulate ReservationsList
    object with all the built-in list methods.
    """

    # Index of element with requested start hour in a line of a reservations file
    INDEXClientNameInReservation = 0

    # Index of element with requested start hour in a line of a reservations file
    INDEXRequestedStartHour = 1

    # Index of element with requested start hour in a line of a reservations file
    INDEXRequestedEndHour = 2

    # Index of circuit id in a line of a reservations file
    INDEXCircuitInReservation = 3

    # Index of circuit length in kms in a line of a reservations file
    INDEXCircuitKmsInReservation = 4

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
            inFile = FileUtil(file_name)

            for line in inFile.getContent():
                reservData = line.rstrip().split(", ")
                reservClient = reservData[ReservationsList.INDEXClientNameInReservation]
                reservRequestedStartTime = Time(reservData[ReservationsList.INDEXRequestedStartHour])
                reservRequestedEndTime = Time(reservData[ReservationsList.INDEXRequestedEndHour])
                reservCircuit = reservData[ReservationsList.INDEXCircuitInReservation]
                reservCircuitKms = reservData[ReservationsList.INDEXCircuitKmsInReservation]
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
