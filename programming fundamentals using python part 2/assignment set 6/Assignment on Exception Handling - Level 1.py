def find_smallest_number(num):
	smallest_number=1
	while(True):
		no_of_factors=find_factors(smallest_number)
		if no_of_factors==num:
			return smallest_number
		else:
			smallest_number+=1

def find_factors(n):
	factors=0
	for i in range(1,n+1):
		if n%i==0:
			factors+=1
	return factors

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num,"divisors is",result)

