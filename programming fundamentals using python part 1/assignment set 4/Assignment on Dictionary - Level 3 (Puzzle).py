def max_frequency_word_counter(data):
    max_word=""
    frequency=0

    list = data.lower().split(" ")
    frq_list=[]

    for word in list:
        count=0
        for word2 in list:
            if word == word2:
                count+=1
        frq_list.append(count)

    words_list=[]
    for i in range(0,len(list)):
        if frq_list[i]==max(frq_list):
            words_list.append(list[i])

    

    frequency=max(frq_list)
    max_word=max(words_list,key=len)

    print(max_word,frequency)
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(max_word,frequency)


#Provide different values for data and test your program.
data="Rain on the green grass and Rain on the tree"
max_frequency_word_counter(data)