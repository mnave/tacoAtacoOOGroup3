#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from Service import Service


class DetailedService(Service):
    def __init__(self, driver, vehicle, service):
        Service.__init__(self, service.getServiceDriver(), service.getServicePlate(), service.getServiceClient(), \
                         service.getServiceDepartHour(), service.getServiceArrivalHour(), service.getServiceCircuit(), \
                         service.getServiceCircuitKms(), service.getServiceDriverStatus())
        self._accumTime = driver.getDriverAccumTime()
        self._vehiclePlate = vehicle.getPlate()
        self._vehicleKmsLeft = vehicle.getVehicleKmsLeft()
        self._vehicleAutonomy = vehicle.getVehicleAutonomy()

    def getAccumTime(self):
        return self._accumTime

    def getVehiclePlate(self):
        return self._vehiclePlate

    def getVehicleKmsLeft(self):
        return self._vehicleKmsLeft

    def getVehicleAutonomy(self):
        return self._vehicleAutonomy

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
            "\nvehiclePlate: " + self._vehiclePlate + \
            "\nvehicleKmsLeft: " + self._vehicleKmsLeft + \
            "\nvehicleAutonomy: " + self._vehicleAutonomy
