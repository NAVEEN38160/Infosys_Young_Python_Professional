class Employee:
    __employee_count=1000
    def __init__(self):
        self.__employee_id=None 
    def generate_employee_id(self):
        Employee.__employee_count+=1
        self.__employee_id='E'+str(Employee.__employee_count)
    def get_employee_id(self):
        return self.__employee_id
class Project:
    def __init__(self,project_id,number_of_employees):
        self.__project_id=project_id
        self.__number_of_employees=number_of_employees
    def update_number_of_employees(self):
        self.__number_of_employees+=1
    def get_project__id(self):
        return self.__project_id
    def get_number_of_employees(self):
        return self.__number_of_employees
class Department:
    
    __dep_project_list=[]
    __employee_dict={}
    @staticmethod
    def add_project(project_list):
        if len(project_list+Department.__dep_project_list)<=5:
            Department.__dep_project_list.extend(project_list)
        else:
            return -1
    @staticmethod
    def add_employee(employee,project_id):
        a=[]
        for i in Department.__dep_project_list:
            a.append(i.get_project__id())
            
        if project_id in a:
            if Department.__dep_project_list[a.index(project_id)].get_number_of_employees()<10:
                employee.generate_employee_id()
                Department.__employee_dict[employee.get_employee_id()]=project_id
                Department.__dep_project_list[a.index(project_id)].update_number_of_employees()
            else:
                return -2
        else:
            return -1