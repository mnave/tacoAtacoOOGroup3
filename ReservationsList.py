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

    Requires: a ReservationsXXYY.txt. In case of file_name = None, can be initiated
    through the UserList constructor. All UserList methods are inherited and thus,
    ReservationsList works as a subclass of UserList.

    Ensures: Each object is a list with all the information for one reservation
    as one can find for each line of the ReservationsXXYY.txt.
    """

    def __init__(self, file_name=None):
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
