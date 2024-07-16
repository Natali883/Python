class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self):
        if self.mileage == 2:
            return f"Это мотоцикл марки {self.name}."
        elif self.mileage == 3:
            return f"Это трицикл марки {self.name}."
        elif self.mileage == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю таких транспортных средств."

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо {self.name} можно брать."
        elif 50001 <= self.mileage <= 100000:
            return f"{self.name} надо внимательно проверить."
        elif 100001 <= self.mileage <= 150000:
            return f"{self.name} надо провести полную диагностику."
        else:
            return f"{self.name} лучше не покупать."


vehicle1 = Vehicle("BMW", 4)
vehicle2 = Vehicle("Audi", 2)
vehicle3 = Vehicle("Mercedes", 3)
vehicle4 = Vehicle("Toyota", 100000)


print(vehicle1.get_vehicle_type())
print(vehicle1.get_vehicle_advice())

print(vehicle2.get_vehicle_type())
print(vehicle2.get_vehicle_advice())

print(vehicle3.get_vehicle_type())
print(vehicle3.get_vehicle_advice())

print(vehicle4.get_vehicle_type())
print(vehicle4.get_vehicle_advice())
