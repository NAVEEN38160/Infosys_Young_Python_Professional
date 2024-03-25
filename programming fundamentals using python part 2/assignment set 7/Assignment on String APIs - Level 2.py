#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]



def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count=0
    for item in ticket_list:
        string_item=item.split(":")
        if string_item[2] == destination:
            count+=1
    return count


def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    final_list=[]

    for item in ticket_list:
        split_item=item.split(":")
        flight_no=split_item[0]
        count=0
        final_str=""
        for item2 in ticket_list:
            if item2.startswith(flight_no):
                count+=1
        final_str+=flight_no+":"+str(count)
        if final_list.count(final_str)<1:
            final_list.append(final_str)

    return final_list


def sort_passenger_list():
    list=find_passengers_per_flight()
    freq=[]
    sorted_list=[]
    for item in list:
        split_item=item.split(":")
        freq.append(int(split_item[1]))
    freq=sorted(freq,reverse=True)
    for i in range(0,len(freq)):
        for j in range(0,len(list)):
            if list[j].endswith(str(freq[i])):
                sorted_list.append(list[j])
        
        
    return sorted_list


#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())