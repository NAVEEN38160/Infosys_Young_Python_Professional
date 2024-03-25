def check_for_ten(num1, num2):
    if num1==10 or num2==10 or num1+num2==10:
        return True
    else:
        return False

print(check_for_ten(10, 9))