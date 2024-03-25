from datetime import datetime,timedelta

class GarmentOrder:
    garment_dict = {"shirt":[45,400,30],"trousers":[250,500,25],"saree":[500,750,10],"jersey": [750,200,5]}
    def __init__(self,cloth_type,no_of_piece):
        self.__cloth_type=cloth_type
        self.__no_of_piece=no_of_piece
        self.__delivery_date = None
        self.__order_date = datetime.now().strftime("%d/%m/%Y")

    def get_cloth_type(self):
        return self.__cloth_type
    def get_no_of_piece(self):
        return self.__no_of_piece
    def get_order_date(self):
        return self.__order_date
    def get_delivery_date(self):
        return self.__delivery_date

    def take_order(self):
        if self.__cloth_type in GarmentOrder.garment_dict and GarmentOrder.garment_dict[self.__cloth_type][0]>=self.__no_of_piece:
            self.update_stock()
            amt = self.calculate_amount()
            return amt
        else:
            return -1

    def calculate_amount(self):
        amount = 0
        for key,value in GarmentOrder.garment_dict.items():
            if key == self.__cloth_type:
               amount = value[1]*self.__no_of_piece
        return amount

    def update_stock(self):
        days_to_del=0
        for key,value in GarmentOrder.garment_dict.items():
            if key == self.__cloth_type:
               days_to_del = value[2]
        self.__delivery_date = (datetime.now() + timedelta(days=days_to_del)).strftime("%d/%m/%Y")
        for key,value in GarmentOrder.garment_dict.items():
            if key == self.__cloth_type:
               value[0] -= self.__no_of_piece

shirt=GarmentOrder("shirt",10)