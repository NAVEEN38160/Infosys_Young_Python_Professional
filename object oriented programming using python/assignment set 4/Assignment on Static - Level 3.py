class ThemePark:
    #dict_of_games contains the game name as key, price/ride and points that can be earned by customer in a list as value
    dict_of_games={"Game1":[35.5,5], "Game2":[40.0,6],"Game3":[120.0,10], "Game4":[60.0,7],"Game5":[25.0,4]}

    @staticmethod
    def validate_game(game_input):
        if game_input in ThemePark.dict_of_games:
            return True
        else:
            return False

    @staticmethod
    def get_points(game_input):
        return ThemePark.dict_of_games[game_input][1]

    @staticmethod
    def get_amount(game_input):
        return ThemePark.dict_of_games[game_input][0]

class Ticket:
    __ticket_count=200

    def __init__(self):
        self.__ticket_id=None
        self.__ticket_amount=0

    def generate_ticket_id(self):
        Ticket.__ticket_count+=1
        self.__ticket_id = Ticket.__ticket_count

    def calculate_amount(self,list_of_games):
        tkt_amt=0
        count = 0
        for game in list_of_games:
            if ThemePark.validate_game(game):
                count+=1
        if count == len(list_of_games):
            for game in list_of_games:
                tkt_amt += ThemePark.dict_of_games[game][0]
            self.__ticket_amount = tkt_amt
            return True
        else:
            return False


    def get_ticket_id(self):
        return self.__ticket_id
    def get_ticket_amount(self):
        return self.__ticket_amount

class Customer:
    def __init__(self,name,list_of_games):
        self.__name=name
        self.__list_of_games=list_of_games
        self.__ticket=Ticket()
        self.__points_earned=0
        self.__food_coupon="No"

    def play_game(self):
        for game in self.__list_of_games:
            if game == "Game3":
                self.__list_of_games.append("Game2")
            if game in ThemePark.dict_of_games:
                self.__points_earned += ThemePark.dict_of_games[game][1]

    def update_food_coupon(self):
        if self.__points_earned > 15 and "Game4" in self.__list_of_games:
            self.__food_coupon = "Yes"

    def book_ticket(self):
        a=self.__ticket.calculate_amount(self.__list_of_games)
        if a :
            self.__ticket.generate_ticket_id()
            self.play_game()
            self.update_food_coupon()
            return True
        else:
            return False


    def get_name(self):
        return self.__name
    def get_list_of_games(self):
        return self.__list_of_games
    def get_ticket(self):
        return self.__ticket
    def get_points_earned(self):
        return self.__points_earned
    def get_food_coupon(self):
        return self.__food_coupon

list1=["Game1","Game3"]
c1 = Customer("Naveen",list1)
