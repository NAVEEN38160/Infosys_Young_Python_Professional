class Bill:
    counter= 1000
    def __init__(self):
        self.__bill_id=None
        self.__bill_amount=None

    def generate_bill_amount(self,item_quantity,items):
        temp_bill=0
        for key,value in item_quantity.items():
            for item in items:
                if key.lower() == (item.get_item_id()).lower():
                   temp_bill+= item_quantity[key]*item.get_price_per_quantity()
        self.__bill_amount=temp_bill
        Bill.counter+=1
        self.__bill_id="B"+str(Bill.counter)

    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount

class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None

    def pays_bill(self,bill):
        self.__payment_status="Paid"
        print(self.get_customer_name())
        print(bill.get_bill_id())
        print(bill.get_bill_amount())

    def get_customer_name(self):
        return self.__customer_name
    def get_payment_status(self):
        return self.__payment_status


class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity

    def get_item_id(self):
        return self.__item_id
    def get_description(self):
        return self.__description
    def get_price_per_quantity(self):
        return self.__price_per_quantity