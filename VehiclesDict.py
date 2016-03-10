from UserDict import UserDict
from headerRelated import removeHeader
from Time import Time
from constants import *
from Vehicle import Vehicle

class VehiclesDict(UserDict):

    def __init__(self, file_name = None):
        UserDict.__init__(self)

        inFile = removeHeader(open(file_name, "r"))
        for line in inFile:
            vehicleData = line.rstrip().split(", ")
            vehiclePlate = vehicleData.pop(INDEXVehiclePlateInDict)
            vehicleModel, vehicleAutonomy, vehicleKms = vehicleData
            newVehicle = Vehicle(vehiclePlate, vehicleModel, vehicleAutonomy, vehicleKms)

            self[vehiclePlate] = newVehicle

    def __str__(self):
        output = ""

        for vehicle in self.values():
            output += vehicle.getPlate() + "\n"

        return output


