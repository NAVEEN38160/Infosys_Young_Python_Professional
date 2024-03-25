def check_double(number):
    num_str=str(number)
    double_str=str(2*number)
    if len(num_str)==len(double_str):
        sum1=0
        for i in range(0,len(num_str)):
            sum1+=int(num_str[i])
        sum2=0
        for j in range(0,len(double_str)):
            sum2+=int(double_str[j])
        if sum1==sum2:
            return True
        else:
            return False
    else:
        return False

print(check_double(125874))