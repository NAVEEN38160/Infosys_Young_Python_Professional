class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__course_id=None
        self.__fees=None

    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False

    def choose_course(self,course_id):
        if course_id==1001:
            self.__course_id=course_id
            if self.__marks>85:
                self.__fees=25575.0-(0.25*25575.0)
            else:
                self.__fees=25575.0
            return True
        elif course_id==1002:
            self.__course_id=course_id
            if self.__marks>85:
                self.__fees=15500.0-(0.25*15500.0)
            else:
                self.__fees=15500.0
            return True
        else:
            return False

    def set_student_id(self,student_id):
        self.__student_id=student_id
    def set_age(self,age):
        self.__age=age
    def set_marks(self,marks):
        self.__marks=marks

    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees
