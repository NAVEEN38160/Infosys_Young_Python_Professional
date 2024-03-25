def list_of_count(word_list):
    count_list=[]
    for word in word_list:
        length=len(word)
        count_list.append(length)
    return count_list

word_list = ["COme", "here"]
print(list_of_count(word_list))