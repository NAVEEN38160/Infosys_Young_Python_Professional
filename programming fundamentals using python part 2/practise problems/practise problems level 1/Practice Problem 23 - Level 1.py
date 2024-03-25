def divisible_by_sum(number):
    str_no=str(number)
    sum=0
    for item in str_no:
        sum+=int(item)
    if number%sum==0:
        return True
    else:
        return False

number = 42
print(divisible_by_sum(number))