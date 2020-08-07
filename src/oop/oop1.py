# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():
    """BASE CLASS"""
    def __init__(self):
        pass


class FlightVehicle(Vehicle):
    """Sub-class of Vehicle"""
    def __init__(self):
        super().__init__()
        pass


class Starship(FlightVehicle):
    """Sub-class of FlightVehicle"""
    def __init__(self):
        super().__init__()
        pass


class Airplane(FlightVehicle):
    """Sub-class of FlightVehicle"""
    def __init__(self):
        super().__init__()
        pass


class GroundVehicle(Vehicle):
    """Sub-class of Vehicle"""
    def __init__(self):
        super().__init__()
        pass


class Car(GroundVehicle):
    """Sub-class of GroundVehicle"""
    def __init__(self):
        super().__init__()
        pass


class Motorcycle(GroundVehicle):
    """Sub-class of GroundVehicle"""
    def __init__(self):
        super().__init__()
        pass
