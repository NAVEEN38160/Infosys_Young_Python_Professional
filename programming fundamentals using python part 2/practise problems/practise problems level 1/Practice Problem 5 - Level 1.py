def count_digits_letters(sentence):
    letters=""
    numbers=""
    for i in range(0,len(sentence)):
        if sentence[i].isalpha():
            letters+=sentence[i]
        if sentence[i].isdigit():
            numbers+=sentence[i]
    result_list=[len(letters),len(numbers)]

    return result_list


sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))