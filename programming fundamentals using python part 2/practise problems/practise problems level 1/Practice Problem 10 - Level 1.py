def string_both_ends(input_string):
    if len(input_string)<2:
        return -1
    first_two=input_string[0:2]
    last_two=input_string[-2:]
    final=first_two+last_two
    return final

input_string="w3w"
print(string_both_ends(input_string))