class Multiplex:

    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[None,None]
    __list_ticket_price=[150,200]

    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None

    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets

    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name not in Multiplex.__list_movie_name:
            return 0
        elif number_of_tickets > Multiplex.__list_total_tickets[Multiplex.__list_movie_name.index(movie_name)]:
            return -1
        else:
            self.__seat_numbers=self.generate_seat_number(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)
            self.calculate_ticket_price(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)

    def  generate_seat_number(self,movie_index, number_of_tickets):
        last_seat=None
        if Multiplex.__list_last_seat_number[movie_index] == None:
            last_seat = 0
        else:
            last_seat = int(Multiplex.__list_last_seat_number[movie_index][3:])
        seat_numbers=[]
        if movie_index==0:
            for i in range(1,number_of_tickets+1):
                seat_numbers.append("M1-"+str(i+last_seat))
        if movie_index==1:
            for i in range(1,number_of_tickets+1):
                seat_numbers.append("M2-"+str(i+last_seat))
        Multiplex.__list_total_tickets[movie_index] -= number_of_tickets
        Multiplex.__list_last_seat_number[movie_index] = seat_numbers[-1]
        return seat_numbers


booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())



print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status2=booking2.book_ticket("movie2",6)
if(status2==0):
    print("invalid movie name")
elif(status2==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())




print("-----------------------------------------------------------------------------")
booking3=Multiplex()
status3=booking3.book_ticket("movie2",6)
if(status3==0):
    print("invalid movie name")
elif(status3==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking3.get_seat_numbers())
    print("Total amount to be paid:", booking3.get_total_price())