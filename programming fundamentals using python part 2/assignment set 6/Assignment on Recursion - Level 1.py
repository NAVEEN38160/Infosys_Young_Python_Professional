def check_pal(word,reverse):
    if word == reverse:
        return True
    else:
        return False
def is_palindrome(word):
    word=word.lower()
    reverse=""
    for i in range(-1,-(len(word)+1),-1):
        reverse+=word[i]
    return check_pal(word,reverse)

result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")