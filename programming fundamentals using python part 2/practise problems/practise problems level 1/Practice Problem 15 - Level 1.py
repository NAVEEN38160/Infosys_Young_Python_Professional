def check_22(num_list):
    count=0
    for i in range(0,len(num_list)-1):
        if num_list[i]==2:
            if num_list[i+1]==2:
                count+=1
    if count>0:
        return True
    else:
        return False

print(check_22([3, 2, 5, 1, 2, 1, 2, 2]))