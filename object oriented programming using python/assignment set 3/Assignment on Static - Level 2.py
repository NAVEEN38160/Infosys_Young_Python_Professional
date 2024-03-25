class Applicant:
    __application_dict={}
    __applicant_id_count=1000
    def __init__(self,applicant_name):
        self.__applicant_name=applicant_name
        self.__applicant_id=None
        self.__job_band=None
    def generate_applicant_id(self):
        if not(Applicant.__applicant_id_count):
            Applicant.__applicant_id_count=1000
        Applicant.__applicant_id_count=Applicant.__applicant_id_count+1
        self.__applicant_id=Applicant.__applicant_id_count
    def apply_for_job(self,job_band):
        try:
            if Applicant.__application_dict[job_band]==5:
                return -1
            Applicant.__application_dict[job_band]+=1
        except:
            Applicant.__application_dict[job_band]=1
        self.generate_applicant_id()
        self.__job_band=job_band
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict
    def get_applicant_id(self):
        return self.__applicant_id
    def get_applicant_name(self):
        return self.__applicant_name
    def get_job_band(self):
        return self.__job_band
a=Applicant('Hi')
a.apply_for_job('A')
print(Applicant.get_application_dict())