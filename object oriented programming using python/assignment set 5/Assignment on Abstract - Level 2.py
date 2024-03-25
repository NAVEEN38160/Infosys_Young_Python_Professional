from abc import ABCMeta,abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification

    def get_job_band(self):
        return self.__job_band
    def get_employee_name(self):
        return self.__employee_name
    def get_basic_salary(self):
        return self.__basic_salary
    def get_qualification(self):
        return self.__qualification

    @abstractmethod
    def validate_job_band(self):
        pass

    @abstractmethod
    def calculate_gross_salary(self):
        pass

    def validate_basic_salary(self):
        if self.__basic_salary > 3000 :
            return True
        else:
            return False

    def validate_qualification(self):
        if self.__qualification=="Bachelors" or self.__qualification=="Masters":
            return True
        else:
            return False

class Graduate(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,cgpa):
        self.__cgpa=cgpa
        super().__init__(job_band,employee_name,basic_salary,qualification)

    def get_cgpa(self):
        return self.__cgpa

    def validate_job_band(self):
        if super().get_job_band() == "A" or super().get_job_band() == "B" or super().get_job_band() == "C":
            return True
        else:
            return False

    def calculate_gross_salary(self):
        validation1 = super().validate_qualification()
        validation2 = super().validate_basic_salary()
        validation3 = self.validate_job_band()
        if validation1 and validation2 and validation3:
            basic= super().get_basic_salary()
            pf = 0.12*basic
            tpi = 0
            incentive = 0
            if super().get_job_band() == "A":
                incentive = 4
            elif super().get_job_band() == "B":
                incentive = 6
            else:
                incentive = 10
            if self.__cgpa>=4 and self.__cgpa<=4.25:
                tpi = 1000
            elif self.__cgpa>=4.26 and self.__cgpa<=4.5:
                tpi = 1700
            elif self.__cgpa>=4.51 and self.__cgpa<=4.75:
                tpi = 3200
            elif self.__cgpa>=4.76 and self.__cgpa<=5:
                tpi = 5000
            gross_salary = basic+pf+tpi+(basic*(incentive/100))
            return gross_salary
        else:
            return -1

class Lateral(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
        self.__skill_set=skill_set
        super().__init__(job_band, employee_name, basic_salary, qualification)

    def get_skill_set(self):
        return self.__skill_set

    def validate_job_band(self):
        if super().get_job_band() == "D" or super().get_job_band() == "E" or super().get_job_band() == "F" :
            return True
        else:
            return False

    def calculate_gross_salary(self):
        validation1 = super().validate_qualification()
        validation2 = super().validate_basic_salary()
        validation3 = self.validate_job_band()
        if validation1 and validation2 and validation3:
            basic = super().get_basic_salary()
            pf = 0.12 * basic
            incentive = 0
            sme = 0
            if super().get_job_band() == "D":
                incentive = 13
            elif super().get_job_band() == "E":
                incentive = 16
            else:
                incentive = 20
            if self.__skill_set == "AGP":
                sme = 6500
            elif self.__skill_set == "AGPT":
                sme = 8200
            elif self.__skill_set == "AGDEV":
                sme = 11500
            gross_salary = basic + pf + sme + ((incentive/100)*basic)
            return gross_salary
        else:
            return -1

