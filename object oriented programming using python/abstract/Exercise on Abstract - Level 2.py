from abc import ABCMeta,abstractmethod

class DirectToHomeService(metaclass=ABCMeta):
    __counter = 101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter += 1

    def get_consumer_number(self):
        return self.__consumer_number
    def get_consumer_name(self):
        return self.__consumer_name

    @abstractmethod
    def calculate_monthly_rent(self):
        pass

class BasePackage(DirectToHomeService):
    def __init__(self,
                 consumer_name,
                 base_pack_name,
                 subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name

    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        if self.__base_pack_name == "Silver" or self.__base_pack_name == "Gold" or self.__base_pack_name == "Platinum":
            pass
        else:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")

    def calculate_monthly_rent(self):
        if self.__subscription_period>=1 and self.__subscription_period<=24:
            self.validate_base_pack_name()
            monthly_rent = 0
            final_rent = 0
            if self.__base_pack_name == "Silver":
                monthly_rent = 350.0
            elif self.__base_pack_name == "Gold":
                monthly_rent = 440.0
            else:
                monthly_rent = 560.0
            if self.__subscription_period > 12:
                final_rent = ((monthly_rent*self.__subscription_period)-monthly_rent)/self.__subscription_period
            else:
                final_rent = monthly_rent 
            return final_rent
        else:
            return -1