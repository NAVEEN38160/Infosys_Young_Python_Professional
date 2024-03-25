class Employee:
    def __init__(self,employee_id,employee_name,smart_card):
        self.__employee_id = employee_id
        self.__employee_name=employee_name
        self.smart_card = smart_card

    def get_employee_id(self):
        return self.__employee_id
    def get_employee_name(self):
        return self.__employee_name

    def validate_employee_id(self):
        if self.__employee_id > 1000 and self.__employee_id<=700000:
            return True
        else:
            return False

    def validate_card_no(self):
        x = self.smart_card.get_card_no()
        if len(x)==9 and x.startswith("INF") and x[3:].isdigit():
            return True
        else:
            return False

class SmartCard:
    def __init__(self,card_no):
        self.__card_no = card_no
        self.__account_balance = 500

    def get_card_no(self):
        return self.__card_no
    def get_account_balance(self):
        return self.__account_balance
    def set_account_balance(self,account_balance):
        self.__account_balance = account_balance

class Transaction:
    def __init__(self):
        self.__transaction_id = None

    def get_transaction_id(self):
        return self.__transaction_id

    def top_up_card(self,employee,amount):
        if amount>=500 and amount<=10000:
            validation1=employee.validate_employee_id()
            validation2 = employee.validate_card_no()
            if validation1 and validation2:
                employee.smart_card.set_account_balance(employee.smart_card.get_account_balance()+amount)
            else:
                return -1
        else:
            return -1

    def make_payment(self,employee,amount):
        balance = employee.smart_card.get_account_balance()
        validation1 = employee.validate_employee_id()
        after_trans_balance = balance - amount
        if balance >= 0 and validation1 and after_trans_balance >= 500:
            employee.smart_card.set_account_balance(after_trans_balance)
            tid1 = str(employee.get_employee_id())[0]
            tid2 = str(employee.smart_card.get_card_no())[3:5]
            self.__transaction_id = "T"+tid1+tid2
        else:
            return -1

naveen = Employee(1111,"naveen",SmartCard("INF123456"))
t=Transaction()
t.top_up_card(naveen,1000)
t.make_payment(naveen,250)

a=naveen.smart_card.get_account_balance()
