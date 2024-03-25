class Dog:
    counter = 100
    dog_breed_dict = {"Labrador Retriever":5,"German Shepherd":12,"Beagle":10}
    def __init__(self,breed_list,accessories_required):
        self.__breed_list=breed_list
        self.__accessories_required=accessories_required
        self.__price = 0
        self.__dog_id_list = []

    def get_dog_id_list(self):
        return self.__dog_id_list
    def get_breed_list(self):
        return self.__breed_list
    def get_price(self):
        return self.__price
    def get_accessories_required(self):
        return self.__accessories_required

    def get_dog_price(self,breed):
        price = 0
        if breed == "Labrador Retriever":
            price = 800
        elif breed == "German Shepherd":
            price = 1230
        else:
            price = 650
        return price

    def generate_dog_id(self,breed):
        first_letter = breed[0]
        Dog.counter += 1
        dog_id = first_letter+str(Dog.counter)
        return dog_id

    def validate_breed(self):
        b = 0
        for breed in self.__breed_list:
            if breed in Dog.dog_breed_dict:
                b += 1
        if b == len(self.__breed_list):
            return True
        else:
            return False

    def validate_quantity(self):
        ya = 0
        val=self.validate_breed()
        if val:
            for breed in self.__breed_list:
                if Dog.dog_breed_dict[breed] > 0 :
                    ya += 1
            if ya == len(self.__breed_list):
                return True
            else:
                return False
        else:
            return False

    def calculate_total_price(self):
        validation1 = self.validate_breed()
        validation2 = self.validate_quantity()
        if validation1:
            if validation2:
                for breed in self.__breed_list:
                    Dog.dog_breed_dict[breed] -= 1
                    id = self.generate_dog_id(breed)
                    self.__dog_id_list.append(id)
                    self.__price += self.get_dog_price(breed)
                if self.__accessories_required:
                    self.__price += 350
                if self.__price > 1500 :
                    self.__price -= self.__price*0.05
            else:
                return -2
        else:
            return -1


