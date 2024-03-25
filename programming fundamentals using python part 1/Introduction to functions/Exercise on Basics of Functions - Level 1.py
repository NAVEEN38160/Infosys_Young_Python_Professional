#lex_auth_01269361601342668881

std_ad=37550.0
std_ch=std_ad/3
service_tax=0.07
discount=0.1

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    adults_price=no_of_adults*std_ad
    child_price=no_of_children*std_ch
    sum_of_both_classes=adults_price+child_price
    with_service_tax=(sum_of_both_classes*service_tax)+sum_of_both_classes
    after_discount=with_service_tax-(with_service_tax*discount)
    total_ticket_cost=after_discount
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)