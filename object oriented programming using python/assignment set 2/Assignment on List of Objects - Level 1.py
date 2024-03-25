class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        for item in list_of_call_string:
            splitted=item.split(",")
            call_obj=CallDetail(splitted[0],splitted[1],splitted[2],splitted[3])
            if self.list_of_call_objects == None:
                self.list_of_call_objects=[]
            self.list_of_call_objects.append(call_obj)


call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)