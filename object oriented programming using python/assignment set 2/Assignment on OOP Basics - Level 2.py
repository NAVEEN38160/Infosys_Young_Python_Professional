class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None

    def validate_flower(self):
        if self.__flower_name=="orchid" or self.__flower_name=="rose" or self.__flower_name=="jasmine":
            return True
        else:
            return False

    def validate_stock(self,required_quantity):
        if self.__stock_available>=required_quantity:
            return True
        else:
            return False

    def sell_flower(self,required_quantity):
        validation1=self.validate_flower()
        validation2=self.validate_stock(required_quantity)
        if validation1 and validation2:
            self.__stock_available=self.__stock_available-required_quantity

    def check_level(self):
        if self.__flower_name=="orchid":
            if self.__stock_available<15:
                return True
            else:
                return False
        elif self.__flower_name=="rose":
            if self.__stock_available<25:
                return True
            else:
                return False
        elif self.__flower_name=="jasmine":
            if self.__stock_available<40:
                return True
            else:
                return False
        else:
            return False

    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name.lower()
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available

    def get_flower_name(self):
        return self.__flower_name
    def get_price_per_kg(self):
        return self.__price_per_kg
    def get_stock_available(self):
        return self.__stock_available


