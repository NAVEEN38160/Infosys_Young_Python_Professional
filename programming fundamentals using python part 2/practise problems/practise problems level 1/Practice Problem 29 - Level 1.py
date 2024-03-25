def exchange_list(number_list):
    temp_list=number_list[:len(number_list)//2]
    temp_list2=[]
    for i in range(-1,-(len(number_list)//2+1),-1):
        temp_list2.append(number_list[i])
    number_list=temp_list2+temp_list
    return number_list

number_list = [1, 2, 3, 4, 5, 6]
print(exchange_list(number_list))