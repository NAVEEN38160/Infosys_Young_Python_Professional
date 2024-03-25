class Consultant:
    def __init__(self,name,registered_company_list,vacancy_list,registered_student_dict):
        self.__name = name
        self.__registered_company_list = registered_company_list
        self.__vacancy_list = vacancy_list
        self.__registered_student_dict = registered_student_dict

    def get_name(self):
        return self.__name
    def get_registered_company_list(self):
        return self.__registered_company_list
    def get_vacancy_list(self):
        return self.__vacancy_list
    def get_registered_student_dict(self):
        return self.__registered_student_dict

    def validate_vacancy(self,company_name):
        if company_name in self.__registered_company_list:
            index = self.__registered_company_list.index(company_name)
            if self.__vacancy_list[index] > 0:
                return index
            else:
                return -1
        else:
            return -1

    def register_student_for_placement(self,index,student_id):
        company = self.__registered_company_list[index]
        self.__vacancy_list[index] -= 1
        self.__registered_student_dict[company].append(student_id)

class Student:
    def __init__(self,name,student_id,branch,aggregate_percentage,year_of_passing):
        self.__name = name
        self.__student_id = student_id
        self.__branch = branch
        self.__aggregate_percentage = aggregate_percentage
        self.__year_of_passing = year_of_passing

    def get_name(self):
        return self.__name
    def get_student_id(self):
        return self.__student_id
    def get_branch(self):
        return self.__branch
    def get_aggregate_percentage(self):
        return self.__aggregate_percentage
    def get_year_of_passing(self):
        return self.__year_of_passing

    def check_eligibility(self):
        if self.__year_of_passing == 2015 and self.__aggregate_percentage >= 65:
            return True
        else:
            return False

    def apply_for_job(self,company_name,consultant):
        vacancy_index = consultant.validate_vacancy(company_name)
        if vacancy_index >= 0:
            if self.check_eligibility():
                consultant.register_student_for_placement(vacancy_index,self.__student_id)
            else:
                return -1
        else:
            return -1