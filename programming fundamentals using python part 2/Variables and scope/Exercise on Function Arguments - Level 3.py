def factorial(number):
    factorial=1
    while number>0:
        factorial*=number
        number-=1
    return factorial

def find_strong_numbers(num_list):
    strong_numbers = []
    for item in num_list:
        string_item=str(item)
        sum_of_fact=0
        for i in range(0,len(string_item)):
            sum_of_fact+=factorial(int(string_item[i]))
        if sum_of_fact == item:
            strong_numbers.append(item)
    return strong_numbers
            
            
num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)