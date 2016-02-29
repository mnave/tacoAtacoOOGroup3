#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from Service import Service


class DetailedService(Service):
    def __init__(self, driver=None, vehicle=None, service=None):
        if driver is None:
            return
        Service.__init__(self, service.getServiceDriver(), service.getServicePlate(), service.getServiceClient(), \
                         service.getServiceDepartHour(), service.getServiceArrivalHour(), service.getServiceCircuit(), \
                         service.getServiceCircuitKms(), service.getServiceDriverStatus())
        self._accumTime = driver.getDriverAccumTime()
     #   self._vehiclePlate = vehicle.getPlate()
        self._vehicleKmsDone = vehicle.getVehicleKmsDone()
        self._vehicleAutonomy = vehicle.getVehicleAutonomy()

    def getAccumTime(self):
        return self._accumTime

#    def getVehiclePlate(self):
#        return self._vehiclePlate

    def getVehicleKmsDone(self):
        return self._vehicleKmsDone

    def getVehicleAutonomy(self):
        return self._vehicleAutonomy

    def calculateKmsLeft(self):
        """Calculates how many kilometers the vehicle of this service can still do."""

        return int(self.getVehicleAutonomy()) - int(self.getVehicleKmsDone())

    def setNewAccumTime(self, newAccumTime):
        self._accumTime = newAccumTime

    def setVehicleAutonomy(self, vehicAutonomy):
        self._vehicleAutonomy = vehicAutonomy

    def setVehicleKmsDone(self,  kmsDone):
        self._vehicleKmsDone = kmsDone


    def __lt__(self, other_detailedService):
        """Services with a lower _servArrivalHour are considered less than ones with a higher
        _servArrivalHour attribute. In case of equal _servArrivalHour values, the lower DetailedService
        if the one with the lower _accumTime. In the case of equal _accumTime values, the lower service
        is the one with the lower _servDriver.
        """

        # compare by arrival hour
        if self.getServiceArrivalHour() < other_detailedService.getServiceArrivalHour():
            return True
        elif self.getServiceArrivalHour() > other_detailedService.getServiceArrivalHour():
            return False
        else:

            # compare by accumulated time
            if self.getAccumTime() < other_detailedService.getAccumTime():
                return True
            elif self.getAccumTime() > other_detailedService.getAccumTime():
                return False
            else:

                # compare by driver name
                if self.getServiceDriver() < other_detailedService.getServiceDriver():
                    return True
                else:
                    return False

    def __str__(self):
        return Service.__str__(self) + \
            "\nAccum Time: " + self._accumTime + \
            "\nvehicleKmsDone: " + str(self._vehicleKmsDone) + \
            "\nvehicleAutonomy: " + str(self._vehicleAutonomy)
