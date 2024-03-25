def find_gcd(num1, num2):
    factors1=[]
    for i in range(1,num1+1):
        if num1%i==0:
            factors1.append(i)
    factors2 = []
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factors2.append(i)
    common_factors=[]
    for i in factors1:
        for j in factors2:
            if i==j:
                common_factors.append(i)
    return max(common_factors)

num1 = 14
num2 = 35
print(find_gcd(num1, num2))