from UserList import UserList
from headerRelated import removeHeader
from constants import *
from Time import Time
from Reservation import Reservation

class ReservationsList(UserList):

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
        output = ""

        for reservation in self:
            output += reservation.getReservClient() + '\n'

        return output


