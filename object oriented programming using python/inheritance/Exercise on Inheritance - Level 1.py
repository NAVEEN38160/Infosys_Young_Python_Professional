class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status=trained_status
        self.__experience=experience

    def rides_vehicle(self):
        print("Riding vehicle")

class BikeRider(Rider):
    def __init__(self,trained_status,experience,race_license):
        super().__init__(trained_status,experience)
        self.__race_license=race_license

    def rides_in_dome(self):
        print("Ridin in dome")

class CycleRider(Rider):
    def rides_blindfolded(self):
        print("Ridin blindfolded")