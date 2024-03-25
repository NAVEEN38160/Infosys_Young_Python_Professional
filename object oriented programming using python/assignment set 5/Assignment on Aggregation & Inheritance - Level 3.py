class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity

    def validate_quantity(self):
        if self.__quantity >=1 and self.__quantity <=5:
            return True
        else:
            return False

    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        self.__quantity

class Pizzaservice:
    counter = 100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer = customer
        self.__pizza_type = pizza_type.lower()
        self.__additional_topping = additional_topping
        self.__service_id = None
        self.pizza_cost = None

    def validate_pizza_type(self):
        if self.__pizza_type == "small" or self.__pizza_type == "medium":
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        validation1 = self.validate_pizza_type()
        validation2 = self.__customer.validate_quantity()
        if validation2 and validation1:
            if self.__pizza_type == "small":
                self.pizza_cost = self.__customer.get_quantity() * 150
                if self.__additional_topping == True :
                    self.pizza_cost += self.__customer.get_quantity() * 35
            if self.__pizza_type == "medium":
                self.pizza_cost = self.__customer.get_quantity() * 200
                if self.__additional_topping == True:
                    self.pizza_cost += self.__customer.get_quantity() * 50
            Pizzaservice.counter+=1
            self.__service_id = self.__pizza_type[0]+str(Pizzaservice.counter)
        else:
            self.pizza_cost = -1

    def get_customer(self):
        return self.__customer
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_additional_topping(self):
        return self.__additional_topping

class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.__delivery_charge=None
        self.__distance_in_kms = distance_in_kms
        super().__init__(customer,pizza_type,additional_topping)

    def validate_distance_in_kms(self):
        if self.__distance_in_kms>=1 and self.__distance_in_kms<=10:
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        validation = self.validate_distance_in_kms()
        if validation:
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.__distance_in_kms <= 5:
                    self.__delivery_charge = 5*self.__distance_in_kms
                elif self.__distance_in_kms >5 :
                    self.__delivery_charge = 25 + ((self.__distance_in_kms-5)*7)
                self.pizza_cost += self.__delivery_charge
        else:
            self.pizza_cost = -1

    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
