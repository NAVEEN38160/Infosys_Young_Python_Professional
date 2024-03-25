def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here

    msg01=msg1.replace(" ","")
    msg02=msg2.replace(" ","")

    main_string=""
    for i in range(0,len(msg01)):
        for j in range(0,len(msg02)):
            if msg01[i] == msg02[j] and main_string.count(msg01[i])<1:
                main_string += msg01[i]
                
    if main_string :
        return main_string
    else :
        return -1

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)