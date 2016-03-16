# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from Time import Time

class Vehicle(object):
    """A tuk tuk from Taco-a-Taco."""

    # Limit of vehicle's autonomy in kms left to be able
    # to be assigned a next service
    AUTONThreshold = 15

    # Duration of the recharging operation
    RECHDURATION = Time("01:00")

    def __init__(self, Plate, Model, Autonomy, Kms_done):
        """Creates a new vehicle.

        Requires: Plate is a string representing the license plate. Model is a string representing
        the model of the vehicle. Autonomy is an int representing the autonomy of the vehicle in kms.
        Kms_done is an int representing the number of kms already done by the vehicle since the last time
        it was charged.
        Ensures: Creation of a new Vehicle object.
        """
        self._plate = Plate
        self._model = Model
        self._autonomy = Autonomy
        self._kms_done = Kms_done

    def getPlate(self):
        """The license plate of the vehicle."""

        return self._plate

    def getVehicleModel(self):
        """The model of the vehicle."""

        return self._model

    def getVehicleAutonomy(self):
        """The autonomy of the vehicle, in kms."""

        return self._autonomy

    def getVehicleKmsDone(self):
        """The number of kms done for the vehicle to reach the autonomy."""

        return self._kms_done

    def setPlate(self, Plate):
        """Set the plate of the vehicle.

        Requires: plate is a string representation of the license plate of the vehicle.
        Ensures: getVehiclePlate == Plate
        """

        self._plate = Plate

    def setVehicleModel(self, Model):
        """Set the model of the vehicle.

        Requires: Model is a string representing the model of the vehicle.
        Ensures: getVehicleModel == Model
        """

        self._model = Model

    def setVehicleAutonomy(self, Autonomy):
        """Set the autonomy of the vehicle.

        Requires: Autonomy is an int representing the autonomy of the vehicle in kms.
        Ensures: getVehicleAutonomy == Autonomy
        """

        self._autonomy = Autonomy

    def setVehicleKmsDone(self, Kms_done):
        """Set the the kms done for the vehicle.

        Requires: Kms_left is an int representing the number of kms left for the vehicle to reach the autonomy.
        Ensures: getVehicle == Kms_done
        """

        self._kms_done = Kms_done

    def __eq__(self, other_vehicle):
        """Returns True if self and other_vehicle plates are equal. False otherwise."""

        if self.getPlate() == other_vehicle.getPlate():
            return True

        return False

    def __lt__(self, other_vehicle):
        """Returns True if self plate is lexicographically smaller than other_vehicle plate. False otherwise."""

        if self.getPlate() < other_vehicle.getPlate():
            return True

        return False

    def __str__(self):
        """A string representation of a vehicle"""

        return "Plate: " + self.getPlate() + "\n" + \
               "Model: " + self.getVehicleModel() + "\n" + \
               "Autonomy: " + self.getVehicleAutonomy() + "\n" + \
               "Kms Done: " + self.getVehicleKmsDone()
