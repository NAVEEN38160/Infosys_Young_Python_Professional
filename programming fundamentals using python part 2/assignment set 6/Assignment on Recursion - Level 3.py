def find_duplicates(list_of_numbers):
    duplicate=[]
    for i in range(0,len(list_of_numbers)):
        for j in range(i+1,len(list_of_numbers)):
            if list_of_numbers[i]==list_of_numbers[j] :
                duplicate.append(list_of_numbers[i])
    duplicate=set(duplicate)
    duplicate=list(duplicate)
    return duplicate

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)