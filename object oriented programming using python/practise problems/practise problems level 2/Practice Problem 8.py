class CabRepository:
    cab_type_list = ["Hatch Back","Sedan","SUV"]
    charge_per_km = [9,12,5]
    no_of_cars = [2,5,10]

class CabService:
    __counter = 1000
    def __init__(self,cab_type,distance_in_kms):
        self.__cab_type=cab_type
        self.__distance_in_kms=distance_in_kms
        self.__service_id = None

    def get_cab_type(self):
        return self.__cab_type
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    def get_service_id(self):
        return self.__service_id
    def get_cab_charge(self):
        pass

    def calculate_waiting_charge(self,waiting_time_mins):
        wt_charge = 0
        if waiting_time_mins <= 30:
            wt_charge = 0
        else :
            wt_charge = (waiting_time_mins-30)*5
        return wt_charge

    def get_cab_charge(self,index):
        return CabRepository.charge_per_km[index]

    def booking(self,waiting_time_mins):
        wt_charge = self.calculate_waiting_charge(waiting_time_mins)
        index = self.check_availability()
        if index != -1:
            cab_charge = self.get_cab_charge(index)
            amt = cab_charge*self.__distance_in_kms
            final = amt + wt_charge
            CabRepository.no_of_cars[index]-=1
            CabService.__counter+=1
            self.__service_id = CabService.__counter
            return final
        else:
            return -1

    def check_availability(self):
        if self.__cab_type in CabRepository.cab_type_list:
            index = CabRepository.cab_type_list.index(self.__cab_type)
            if CabRepository.no_of_cars[index]>0:
                return index
            else:
                return -1
        else:
            return -1

