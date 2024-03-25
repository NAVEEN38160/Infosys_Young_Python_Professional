class Buyer:
    def __init__(self,name,email_id):
        self.__name = name
        self.__email_id = email_id

    def get_name(self):
        return self.__name
    def get_email_id(self):
        return self.__email_id

    def purchase(self,item_name,quantity,emi):
        if item_name in OnlinePortal.item_list:
            index = OnlinePortal.item_list.index(item_name)
            if OnlinePortal.quantity_list[index] >= quantity:
                cost = OnlinePortal.place_order(index,emi,quantity)
                return cost
            else:
                return -1
        else:
            return -2

class OnlinePortal:
    item_list = []
    quantity_list = []
    price_list = []

    @staticmethod
    def search_item(item):
        if item in OnlinePortal.item_list:
            index = OnlinePortal.item_list.index(item)
            return index
        else:
            return -1

    @staticmethod
    def place_order(index,emi,quantity):
        OnlinePortal.quantity_list[index] -= quantity
        total_price = OnlinePortal.price_list[index]*quantity
        if emi:
            total_price += 0.02*total_price
        else:
            total_price -= 0.02*total_price
        return total_price

    @staticmethod
    def add_stock(item_name,quantity):
        if item_name in OnlinePortal.item_list:
            index = OnlinePortal.item_list.index(item_name)
            if OnlinePortal.quantity_list[index] <= 10 :
                OnlinePortal.quantity_list[index] += quantity
            else:
                return -1
        else:
            return -2

    @staticmethod
    def add_item(item_name,price,quantity):
        if item_name not in OnlinePortal.item_list:
            OnlinePortal.item_list.append(item_name)
            OnlinePortal.quantity_list.append(quantity)
            OnlinePortal.price_list.append(price)
        else:
            return -2