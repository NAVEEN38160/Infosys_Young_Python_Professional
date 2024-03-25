def find_pairs_of_numbers(num_list,n):
    pairs=[]
    for i in range(0,len(num_list)):
        for j in range(0,len(num_list)):
            if num_list[i]+num_list[j]==n:
                pairs.append(num_list[i])
    
    return len(pairs)//2

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))