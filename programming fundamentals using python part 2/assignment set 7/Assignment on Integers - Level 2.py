def find_palindrome(number):
    str_num=str(number)
    reverse=""
    for i in range(-1,-(len(str_num)+1),-1):
        reverse+=str_num[i]
    if reverse==str_num:
        return True
    else:
        return False

def nearest_palindrome(number):
    n=number+1
    while(True):
        answer=find_palindrome(n)
        if answer :
            return n
        else:
            n+=1

number=99
print(nearest_palindrome(number))