#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func == odd:
        odd_list=odd(list_of_num)
        odd_sum=0
        for item in odd_list:
            odd_sum+=item
        return odd_sum
    elif filter_func == even:
        even_list=even(list_of_num)
        even_sum=0
        for item in even_list:
            even_sum+=item
        return even_sum
    else:
        normal_sum=0
        for item in list_of_num:
            normal_sum+=item
        return normal_sum
            
def even(data):
    even=[]
    for item in data:
        if item%2==0:
            even.append(item)
    return even

def odd(data):
    odd = []
    for item in data:
        if item % 2 != 0:
            odd.append(item)
    return odd

sample_data = range(1,11)
print(sum_of_numbers(sample_data,None))