class Scanner:
    def __init__(self,emp_laptop_dict):
        self.__emp_laptop_dict = emp_laptop_dict

    def scan(self,empid,laptop):
        if empid in self.__emp_laptop_dict :
            if laptop.get_expiry():
                return False
            else:
                return True
        else:
            return False

class Laptop:
    def __init__(self,grcode,expiry):
        self.__grcode=grcode
        self.__expiry=expiry

    def get_expiry(self):
        return self.__expiry
    def get_grcode(self):
        return self.__grcode
