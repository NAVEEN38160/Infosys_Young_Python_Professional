def next_ducci(given_list):
    ducci_items=[]
    for i in range(0,4):
        if i == 3:
            ducci_items.append(given_list[i] - given_list[0])
        else:
            ducci_items.append(abs(given_list[i] - given_list[i + 1]))
    return ducci_items

def ducci_sequence(test_list, n):
    final_list=[]
    input_list=test_list
    for i in range(0,n+1):
        ducci=[]
        ducci=next_ducci(input_list)
        final_list.append(ducci)
        input_list=ducci
    return final_list[n]

ducci_element = ducci_sequence([7, 60, 861, 3070], 3)
print(ducci_element)

print(next_ducci([7, 60, 861, 3070]))



