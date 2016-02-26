#-*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

from constants import *
from calculations import add

class Service(object):
    def __init__(self, servDriver, servPlate, servClient, servDepartHour, servArrivalHour, servCircuit, \
                 servCircuitKms, servDriverStatus):
        self._servDriver = servDriver
        self._servPlate = servPlate
        self._servClient = servClient
        self._servDepartHour = servDepartHour
        self._servArrivalHour = servArrivalHour
        self._servCircuit = servCircuit
        self._servCircuitKms = servCircuitKms
        self._servDriverStatus = servDriverStatus

    def getServiceDriver(self):
        return self._servDriver

    def getServicePlate(self):
        return self._servPlate

    def getServiceClient(self):
        return self._servClient

    def getServiceDepartHour(self):
        return self._servDepartHour

    def getServiceArrivalHour(self):
        return self._servArrivalHour

    def getServiceCircuit(self):
        return self._servCircuit

    def getServiceCircuitKms(self):
        return self._servCircuitKms

    def getServiceDriverStatus(self):
        return self._servDriverStatus

    def setServiceDriver(self, servDriver):
        self._servDriver = servDriver

    def setServicePlate(self, servPlate):
        self._servPlate = servPlate

    def setServiceClient(self, servClient):
        self._servClient = servClient

    def setServiceDepartHour(self, servDepartHour):
        self._servDepartHour = servDepartHour

    def setServiceArrivalHour(self, servArrivalHour):
        self._servArrivalHour = servArrivalHour

    def setServiceCircuit(self, servCircuit):
        self._servCircuit = servCircuit

    def setServiceCircuitKms(self, servCircuitKms):
        self._servCircuitKms = servCircuitKms

    def setServiceDriverStatus(self, servDriverStatus):
        self._servDriverStatus = servDriverStatus

    def resetVehic(self):
        """Changes the status of a driver/vehicle to 'standby'."""

        self.setServiceDriverStatus(STATUSStandBy)

    def afterCharge(self):
        """Updates a service to a after charge status."""

        self.setServiceDriver(NOCLIENT)
        self.setServiceArrivalHour(add(self.getServiceArrivalHour(), "01:00"))
        self.setServiceDepartHour(self.getServiceArrivalHour())
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(STATUSStandBy)

    def noService(self):
        """Update a service's list when there is no service."""

        self.setServiceClient(NOCLIENT)
        self.setServiceCircuit(NOCIRCUIT)
        self.setServiceCircuitKms("0")
        self.setServiceDriverStatus(STATUSStandBy)

    def __lt__(self, other_service):
        """Services with a lower _servArrivalHour are considered less than ones with a higher
        _servArrivalHour attribute. In case of equal _servArrivalHour values, the lower service
        is the one with the lower _servDriver.
        """

        # compare by arrival hour
        if self.getServiceArrivalHour() < other_service.getServiceArrivalHour():
            return True
        elif self.getServiceArrivalHour() == other_service.getServiceArrivalHour():
            # compare by driver name
            if self.getServiceDriver() < other_service.getServiceDriver():
                return True
            else:
                return False
        else:
            return False

    def __getitem__(self, item):
        if item =="servArrivalHour":
            return self._servArrivalHour

        if item == "DriverName":
            return self._servDriver

    def __str__(self):
        """String representation of the service."""

        return "Driver: " + self.getServiceDriver() + \
               "\nPlate: " + self.getServicePlate() + \
               "\nClient: " + self.getServiceClient() + \
               "\nDepartHour: " + self.getServiceDepartHour() + \
               "\nArrivalHour: " + self.getServiceArrivalHour() + \
               "\nCircuit: " + self.getServiceCircuit() + \
               "\nCircuit Kms: " + str(self.getServiceCircuitKms()) + \
               "\nDriver Status: " + self.getServiceDriverStatus()






#herrança da class Service; macaquice para criar já a detailedServiceList do ConstulStatus
class DetailedService(Service):
    def __init__(self, driver, vehicle, service):
        Service.__init__(self, service.getServiceDriver(),service.getServicePlate(),service.getServiceClient(),\
                         service.getServiceDepartHour(),service.getServiceArrivalHour(),service.getServiceCircuit(),\
                         service.getServiceCircuitKms(),service.getServiceDriverStatus())
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
        return Service.__str__(self)+\
            "\nAccum Time: "+self._accumTime+\
            "\nvehiclePlate: "+self._vehiclePlate+\
            "\nvehicleKmsLeft: " + self._vehicleKmsLeft+\
            "\nvehicleAutonomy: " + self._vehicleAutonomy


    def __getitem__(self, item):
        if item =="accumTime":
            return self._accumTime

        if item =="servArrivalHour":
            return self._servArrivalHour

        if item == "DriverName":
            return self._servDriver
