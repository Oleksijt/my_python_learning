
class Car(object):

    def __init__(self, model, year, max_speed, car_type='Not defined'):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.car_type = car_type

    def get_car_type(self):
        return self.car_type.title()

    def change_type(self, new_type):
        self.car_type = new_type

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed

    def set_car_type(self, car_type_needed):
        for subclass in Car.__subclasses__():
            temp_object = subclass(self.model, self.year, self.max_speed)
            if car_type_needed.title() == temp_object.__dict__['car_type']:
                self = temp_object
                return self


class CarGas(Car):

    def __init__(self, model, year, max_speed):
        super(CarGas, self).__init__(model, year, max_speed)
        self.car_type = 'Gas'


class CarPetrol(Car):

    def __init__(self, model, year, max_speed):
        super(CarPetrol, self).__init__(model, year, max_speed)
        self.car_type = 'Petrol'


class CarElectro(Car):

    def __init__(self, model, year, max_speed):
        super(CarElectro, self).__init__(model, year, max_speed)
        self.car_type = 'Electro'


car_bmw = Car('BMW', 2018, 280, 'gas')

print(car_bmw.get_car_type())  # 'Gas'
car_bmw.change_type('petrol')
print(car_bmw.get_car_type())  # 'Petrol'



car_ford_gas = CarGas('Ford', 2005, 210)

print(car_ford_gas.get_car_type())  # 'Gas'
car_ford_gas.change_type('petrol')
print(car_ford_gas.get_car_type())  # 'Petrol'

car_nissan_electro = CarElectro('Nissan', 2016, 190)

print(car_nissan_electro.get_car_type())  # 'Electro'
car_nissan_electro.change_type('petrol')
print(car_nissan_electro.get_car_type())  # 'Petrol'

car = Car('BMW', 2018, 300)

petrol_car = car.set_car_type('petrol')

print(123)
print(petrol_car.__class__)

print(petrol_car.get_model())  # 'BMW'
print(petrol_car.get_year())  # 2018
print(petrol_car.get_max_speed())  # 300
print(petrol_car.get_car_type())  # 'Petrol'

gas_car = car.set_car_type('gas')

print(gas_car.get_car_type())  # 'Gas'
