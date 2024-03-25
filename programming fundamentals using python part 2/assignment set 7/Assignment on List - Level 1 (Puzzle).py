def check_perfect_number(number):
    if number==0:
        return False
    factors=[]
    for i in range(1,number):
        if number%i==0:
            factors.append(i)
    sum=0
    for i in range(0,len(factors)):
        sum+=factors[i]
    if sum == number:
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    final_list=[]
    for i in range(0,len(no_list)):
        answer=check_perfect_number(no_list[i])
        if answer:
            final_list.append(no_list[i])
    return final_list

perfectno_list=check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)