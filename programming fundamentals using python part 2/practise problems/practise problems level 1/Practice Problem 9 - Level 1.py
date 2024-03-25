def generate_dict(number):
    n=1
    new_dict={}
    while(True):
        if n<=number:
            new_dict.update({n:n*n})
            n+=1
        else:
            return new_dict
    return new_dict

number = 20
print(generate_dict(number))