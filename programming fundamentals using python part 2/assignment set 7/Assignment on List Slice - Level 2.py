import math
def check_prime(number):
    factors=[]
    for i in range(2,number+1):
        if number%i==0:
            factors.append(i)
    if len(factors)==1:
        return True
    else:
        return False

def rotations(num):
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    str_num=str(num)
    rotated_list=[num]
    rot_num=num
    for i in range(1,len(str_num)):
        first_digit=int(rot_num//math.pow(10,len(str_num)-1))
        next_few_digits=int(rot_num%math.pow(10,len(str_num)-1))
        rot_num=(next_few_digits*10)+first_digit
        rotated_list.append(rot_num)
    return rotated_list

def get_circular_prime_count(limit):
    final_list=[]
    for i in range(1,limit):
        rotation=rotations(i)
        count=0
        for item in rotation:
            prime=check_prime(item)
            if prime:
                count+=1
        if count==len(rotation):
            final_list.append(i)
    return len(final_list)

print(get_circular_prime_count(100))




