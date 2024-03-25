class Apparel:
    counter = 100
    def __init__(self,price,item_type):
        self.__price=price
        self.__item_type=item_type
        self.__item_id=None
        if item_type=="Cotton":
            Apparel.counter += 1
            self.__item_id="C"+str(Apparel.counter)
        elif item_type=="Silk":
            Apparel.counter += 1
            self.__item_id="S"+str(Apparel.counter)

    def calculate_price(self):
        self.__price += 0.05 * self.__price

    def get_item_id(self):
        self.__item_id
    def get_price(self):
        return self.__price
    def get_item_type(self):
        return self.__item_type
    def set_price(self,price):
        self.__price=price

class Cotton(Apparel):
    def __init__(self,price,discount):
        super().__init__(price, "Cotton")
        self.__discount=discount

    def calculate_price(self):
        super().calculate_price()
        price = super().get_price()
        price -= price*self.__discount/100
        price += 0.05*price
        super().set_price(price)

    def get_discount(self):
        return self.__discount

class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price, "Silk")
        self.__points=None

    def calculate_price(self):
        super().calculate_price()
        price = super().get_price()
        if price > 10000 :
            self.__points = 10
        else:
            self.__points = 3
        price += 0.1*price
        super().set_price(price)

    def get_points(self):
        return self.__points



c=Cotton(8000,2)
a=c.calculate_price()