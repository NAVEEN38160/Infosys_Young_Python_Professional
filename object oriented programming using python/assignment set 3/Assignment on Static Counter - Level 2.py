class Ticket:
    counter = 0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name = passenger_name
        self.__source= source.lower()
        self.__destination = destination.lower()
        self.__ticket_id = None

    def validate_source_destination(self):
        if self.__source == "delhi":
            if self.__destination == "pune" or self.__destination=="chennai" or self.__destination == "mumbai" or self.__destination=="kolkata":
                return True
            else:
                return False
        else:
            return False

    def generate_ticket(self):
        validation=self.validate_source_destination()
        if validation:
            Ticket.counter+=1
            self.__ticket_id=self.__source[0]+self.__destination[0]+f'{Ticket.counter:02}'
        else:
            self.__ticket_id=None


    def get_ticket_id(self):
        return self.__ticket_id
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination