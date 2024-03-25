def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here

    src = source[0:3]
    des = destination[0:3]

    for index in range(0,no_of_passengers):
        tkt = airline+":"+src+":"+des+":"+str(index+101)
        ticket_number_list.append(tkt)


    #Use the below return statement wherever applicable
    if len(ticket_number_list) >5 :
        return ticket_number_list[-5:]

    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))