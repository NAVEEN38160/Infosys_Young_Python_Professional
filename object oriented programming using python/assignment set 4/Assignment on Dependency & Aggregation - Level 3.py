class FruitInfo():
    __fruit_name_list=["Apple","Guava","Orange","Grape","Sweet Lime"]
    __fruit_price_list=[200,80,70,110,60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            return FruitInfo.__fruit_price_list[FruitInfo.__fruit_name_list.index(fruit_name)]
        else:
            return -1

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

class Purchase:
    __counter = 101
    def __init__(self,customer,fruit_name,quantity):
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity
        self.__purchase_id=None

    def get_purchase_id(self):
        return self.__purchase_id
    def get_quantity(self):
        return self.__quantity
    def get_customer(self):
        return self.__customer

    def calculate_price(self):
        fruit = FruitInfo.get_fruit_price(self.__fruit_name)
        if fruit != -1:
            price = fruit*self.__quantity
            if fruit == max(FruitInfo.get_fruit_price_list()) and self.__quantity>1:
                price -= 0.02*price
            elif fruit == min(FruitInfo.get_fruit_price_list()) and self.__quantity>=5:
                price -= 0.05 * price
            if self.__customer.get_cust_type() == "wholesale":
                price -= 0.1*price
            self.__purchase_id = "P"+str(Purchase.__counter)
            Purchase.__counter+=1
            return price
        else:
            return -1


class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type