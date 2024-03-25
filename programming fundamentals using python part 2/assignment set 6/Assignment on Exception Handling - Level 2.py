def find_ten_substring(num_str):
    master_list=[]
    final_list=[]
    for i in range(0,len(num_str)):
        for j in range(i,len(num_str)):
            master_list.append(num_str[i:j+1])
    for item in master_list:
        sum=0
        for i in range(0,len(item)):
            sum+=int(item[i])
        if sum==10 :
            final_list.append(item)
    return final_list

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)