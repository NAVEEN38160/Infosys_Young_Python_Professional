class Letter:
    counter=1
    def __init__(self,sender_area,receiver_area):
        self.__sender_area=sender_area
        self.__receiver_area=receiver_area
        self.letter_id=Letter.counter
        Letter.counter+=1
    def get_sender_area(self):
        return self.__sender_area
    def get_receiver_area(self):
        return self.__receiver_area
class PostMan:
    counter=100
    def __init__(self,name):
        self.__name=name
        self.__post_list_to_deliver=[]
        PostMan.counter+=1
        self.postman_id='P'+str(PostMan.counter)
    def get_name(self):
        return self.__name
    def get_post_list_to_deliver(self):
        return self.__post_list_to_deliver
class PostOffice:
    def __init__(self,area_list,postmen_list):
        self.__area_list=area_list
        self.__postmen_list=postmen_list
    def validate_letter(self,letter):
        if letter.get_receiver_area() in self.__area_list:
            return self.__area_list.index(letter.get_receiver_area())
        return -1
    def allocate_posts(self,letter_list):
        l=[]
        for i in letter_list:
            a=self.validate_letter(i)
            if a!=-1:

                self.__postmen_list[a].get_post_list_to_deliver().append(i)

            else:
                l.append(i)
        return l
    def get_area_list(self):
        return self.__area_list
    def get_postmen_list(self):
        return self.__postmen_list