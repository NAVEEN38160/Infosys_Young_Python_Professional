def find_max(num1, num2):
    max_num = -1
    list1 = []
    
    if num1 < num2:
        for num in range(num1, num2 + 1):
            sum1 = 0
            for i in str(num):
                sum1 = sum1 + int(i)
            if sum1 % 3 == 0 and (num > 9 and num <= 99) and num % 5 == 0:
                list1.append(num)
    else:
        return max_num
    
    if len(list1) > 0:
        max_num = max(list1)
    
    return max_num

# Provide different values for num1 and num2 and test your program.
max_num = find_max(10, 100)

print(max_num)

