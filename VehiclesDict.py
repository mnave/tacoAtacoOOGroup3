# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave


from UserDict import UserDict
from headerRelated import removeHeader
from constants import *
from Vehicle import Vehicle


class VehiclesDict(UserDict):

    """A collection of Vehicles. The behaviour of this collection is similar to the one of the dict type"""

    def __init__(self, file_name=None):
        """Creates a VehicleDict composed by vehicles objects,
        from a file with a list of vehicles.

        Requires: If given, file_name is str with the name of a .txt file containing
        a list of vehicles organized as in the examples provided in
        the general specification (omitted here for the sake of readability).
        Ensures:
        if file_name is given:
            a VehiclesDict, composed by objects of class Vehicle that correspond to the vehicles listed
            in file with name file_name.
        if file_name is none:
            a empty ServiceList.
        """
        UserDict.__init__(self)

        inFile = removeHeader(open(file_name, "r"))
        for line in inFile:
            vehicleData = line.rstrip().split(", ")
            vehiclePlate = vehicleData.pop(INDEXVehiclePlateInDict)
            vehicleModel, vehicleAutonomy, vehicleKms = vehicleData
            newVehicle = Vehicle(vehiclePlate, vehicleModel, vehicleAutonomy, vehicleKms)

            self[vehiclePlate] = newVehicle

    def __str__(self):
        """String representation of the ServiceList. Returns the vehicles plates."""

        output = ""

        for vehicle in self.values():
            output += vehicle.getPlate() + "\n"

        return output
