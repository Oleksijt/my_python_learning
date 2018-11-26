""" This code creates class Car and derived classes for car types.
 Base class contain:
Fields:
 - type (gas, electro, petrol)
 - model
 - year
 - max speed.
Methods:
 - get car type
 - change car type
 - change car class
 - get car model
 - get car year
 - get car max speed
"""

import inspect
import sys


class Car:
    """Base class for autos."""
    car_type = 'Car'

    def __init__(self, model, year, max_speed, car_type="Car"):
        self.car_type = car_type
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def change_type(self, car_type):
        # Changes only car_type parameter without class changing.
        self.car_type = car_type

    def set_car_type(self, new_type):
        # Creates new object from self with the same parameters.
        for key, data in inspect.getmembers(sys.modules[__name__], inspect.isclass):
            if data.car_type == new_type.title():
                new_object = data(self.model, self.year, self.max_speed)
                break
        else:
            new_object = Car(self.model, self.year, self.max_speed)
            print('Class for new car type not found. Base class set.')
        return new_object

    def get_car_type(self):
        return self.car_type.title()

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed


class GasCar(Car):
    """Gas car class."""
    car_type = 'Gas'

    def __init__(self, model, year, max_speed):
        Car.__init__(self, model, year, max_speed, self.car_type)


class ElectroCar(Car):
    """Electro car class."""
    car_type = 'Electro'

    def __init__(self, model, year, max_speed):
        Car.__init__(self, model, year, max_speed, self.car_type)


class PetrolCar(Car):
    """Petrol car class."""
    car_type = 'Petrol'

    def __init__(self, model, year, max_speed):
        Car.__init__(self, model, year, max_speed, self.car_type)


if __name__ == '__main__':
    # Create new object 'Car'.
    car1 = Car('BMW', 2018, 280, 'gas')
    print(car1.get_car_type())

    # Change type of object 'Car'.
    car1.change_type('petrol')
    print(car1.get_car_type())

    # Create  new object 'Car'.
    car = Car('BMW', 2018, 300)
    print(car, car.__dict__)

    # Create similar object class in new class
    petrol_car = car.set_car_type('petroewhgtl')  # It returns Car instance.
    print(petrol_car, petrol_car.__dict__)
    petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
    print(petrol_car, petrol_car.__dict__)
    print(petrol_car.get_model())  # Returns `BMW`
    print(petrol_car.get_year())  # Returns 2018
    print(petrol_car.get_max_speed())  # Returns 300
    print(petrol_car.get_car_type())  # Returns Petrol
    gas_car = car.set_car_type('gas')  # It returns `GasCar` instance
    print(gas_car, gas_car.__dict__)
    print(gas_car.get_car_type())  # Returns Gas
    print(petrol_car)
    print(car)
