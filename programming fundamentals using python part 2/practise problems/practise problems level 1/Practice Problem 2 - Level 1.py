def bracket_pattern(input_str):
    input_str_first_element=input_str[0]
    input_str_last_element=input_str[-1]
    if input_str_first_element == ")":
        return False
    if input_str_last_element == "(":
        return False
    count1=0
    count2=0
    for i in range(0,len(input_str)):
        if input_str[i]=="(":
            count1+=1
        if input_str[i]==")":
            count2+=1
    if count1==count2:
        return True
    else:
        return False

input_str = "())))"
print(bracket_pattern(input_str))