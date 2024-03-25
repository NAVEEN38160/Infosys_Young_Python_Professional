def validate_credit_card_number(card_number):
    card_no=str(card_number)
    reverse_digits=[]
    for i in range(-2,-(len(card_no)+1),-2):
        reverse_digits.append(int(card_no[i]))
    for i in range(0,len(reverse_digits)):
        reverse_digits[i]=reverse_digits[i]*2
    for i in range(0,len(reverse_digits)):
        if reverse_digits[i]>9:
            str_no=str(reverse_digits[i])
            sum=0
            for j in range(0,len(str_no)):
                sum+=int(str_no[j])
            reverse_digits[i]=sum
    sum_of_rev_digits=0
    for i in range(0,len(reverse_digits)):
        sum_of_rev_digits+=reverse_digits[i]
    normal_numbers=[]
    for i in range(-1,-(len(card_no)+1),-2):
        normal_numbers.append(int(card_no[i]))
    sum_of_norm_digits=0
    for i in range(0,len(normal_numbers)):
        sum_of_norm_digits+=normal_numbers[i]
    final_sum=sum_of_norm_digits+sum_of_rev_digits
    if final_sum%10==0:
        return True
    else:
        return False

card_number= 1456734512345698
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")