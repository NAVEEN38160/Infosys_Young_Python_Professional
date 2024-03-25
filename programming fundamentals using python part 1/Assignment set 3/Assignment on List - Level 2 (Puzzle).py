def create_largest_number(number_list):

    #remove pass and write your logic here
    
    number_list.sort()
    number_list.reverse()
    line = ""
    for i in range(0,len(number_list)):
        line += str(number_list[i])

    integer = int(line)
    return integer


number_list=[98,10,22]
largest_number=create_largest_number(number_list)
print(largest_number)