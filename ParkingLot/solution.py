# To understand the inner workings of OOP : 

from enum import Enum
import random

# This is the vehicle type class for what all type of vehicles can
# for parking
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    BUS = 3

class Vehicle:
    
    def __init__(self,licensePlate,companyName,type_of_vehicle):
        self.licensePlate = licensePlate
        self.companyName = companyName
        self.type_of_vehicle = type_of_vehicle
        
    def getType(self):
        return self.type_of_vehicle
    
    """
    Overwrite __eq__ methods to correctly check if two vehicle objects
    are the same
    """
    
    def __eq__(self,other):
        if other is None:
            return False
        if self.licensePlate != other.licensePlate:
            return False
        if self.companyName != other.companyName:
            return False
        if self.type_of_vehicle != other.type_of_vehicle:
            return False
        return True

#Car Class that inherits the vehicle class
class Car(Vehicle):
    def __init__(self,licensePlate,companyName):
        Vehicle.__init__(self,licensePlate,companyName,VehicleType.CAR)


class Bike(Vehicle):
    def __init__(self,licensePlate,companyName):
        Vehicle.__init__(self,licensePlate,companyName,VehicleType.BIKE)


class Bus(Vehicle):
    def __init__(self,licensePlate,companyName):
        Vehicle.__init__(self,licensePlate,companyName,VehicleType.BUS)
        
    
        
class Slots:
    def __init__(self,lane,spotNumber,type_of_vehicle):
        self.lane = lane
        self.spotNumber = spotNumber
        self.vehicle = None
        self.type_of_vehicle = type_of_vehicle

    def isAvailable(self):
        return self.vehicle == None
    
    def park(self,vehicle):
        if vehicle.type_of_vehicle == self.type_of_vehicle:
            self.vehicle = vehicle
            return True
        return False
    
    def removeVehicle(self):
        self.vehicle = None
        return self.vehicle
    
    def getVehicle(self):
        return self.vehicle


class Levels:
    def __init__(self,floorNumber,no_of_slots):
        self.floorNumber = floorNumber
        self.spots_per_lane = 10
        self.lanes = no_of_slots / self.spots_per_lane
        self.parkingSlots = set()
        self.availableSpots = []
        
        # Check available spots in a lane
        for lane in range(int(self.lanes)):
            for i in range(self.spots_per_lane):
                self.availableSpots.append(Slots(lane,i,random.choice(list(VehicleType))))
                
    
    
        
