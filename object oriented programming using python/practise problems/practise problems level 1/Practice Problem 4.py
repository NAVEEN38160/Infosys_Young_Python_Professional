class Tollbooth:
    def __init__(self):
        self.__no_of_vehicle = 0
        self.__total_amount = 0

    def calculate_amount(self,vehicle_type):
        vehicle_type = vehicle_type.lower()
        if vehicle_type == "car":
            self.__total_amount += 70
        elif vehicle_type == "bus":
            self.__total_amount += 100
        elif vehicle_type == "truck":
            self.__total_amount += 150
        else:
            self.__total_amount += 70

    def count_vehicle(self):
        self.__no_of_vehicle += 1

    def collect_toll(self,owner_type,vehicle_type):
        owner_type = owner_type.lower()
        if owner_type == "vip":
            self.count_vehicle()
        else:
            self.calculate_amount(vehicle_type)
            self.count_vehicle()

    def get_no_of_vehicle(self):
        return self.__no_of_vehicle

    def get_total_amount(self):
        return self.__total_amount

