def find_upper_and_lower(sentence):
    lower=0
    upper=0
    for letter in sentence:
        if letter.islower():
            lower+=1
        if letter.isupper():
            upper+=1
    result_list=[upper,lower]
    return result_list

sentence = "Come Here"
print(find_upper_and_lower(sentence))