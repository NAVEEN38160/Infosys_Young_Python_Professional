def sum_of_elements(num_list, number):
    filtered_list=[]
    for i in range(0,len(num_list)):
        if i==len(num_list)-1:
            if not(num_list[i]==number or num_list[i-1]==number):
                filtered_list.append(num_list[i])
        else:
            if not(num_list[i]==number or num_list[i+1]==number or num_list[i-1]==number):
                filtered_list.append(num_list[i])
    sum=0
    for item in filtered_list:
        sum+=item
    return sum
        
num_list = [1, 7, 3, 4, 1, 7, 10, 5]
number = 7
print(sum_of_elements(num_list, number))