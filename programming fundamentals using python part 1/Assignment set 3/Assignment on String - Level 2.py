def encode(message):

    #Remove pass and write your logic here

    encoded_string = ""
    count = 1

    for i in range(1, len(message)):
        # If the current character is the same as the previous one, increase the count
        if message[i] == message[i - 1]:
            count += 1
        else:
            # Append the character and its count to the encoded string
            encoded_string +=  str(count)+message[i - 1]
            count = 1

    encoded_string +=  str(count)+message[-1]

    return encoded_string

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)



