class Vehicle:
    def __init__(self):
        self.mileage=None
        self.fuel_left=None

    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left - 5 > 0:
            return (self.fuel_left - 5) * self.mileage
        else:
            return 0

    def identify_distance_travelled(self,initial_fuel):
        trip_meter=(initial_fuel-self.fuel_left)*self.mileage
        return trip_meter


car = Vehicle()
car.mileage = 10
car.fuel_left = 20
print(car.identify_distance_that_can_be_travelled())
print(car.identify_distance_travelled(100))


