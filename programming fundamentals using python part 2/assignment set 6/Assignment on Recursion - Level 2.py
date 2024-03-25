def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor
    prime_number=0
    for i in range(0,len(list_of_factors)):
        if is_prime(list_of_factors[i],list_of_factors[i]//2):
            prime_number=list_of_factors[i]
    return prime_number

def find_f(num):
    #Accepts the number and returns the largest prime factor of the number
    list_of_factors=find_factors(num)
    return find_largest_prime_factor(list_of_factors)
    
def find_g(num):
#Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    sum=0
    for i in range(num,num+9):
        sum+=find_f(i)
    return sum
#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))

