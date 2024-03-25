def check_palindrome(word):

    #Remove pass and write your logic here
    reverse = ""

    for index in range(-1,-(len(word)+1),-1):
        reverse += word[index]
        
    
    if reverse == word:
        return True
    else:
        return False
        

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")