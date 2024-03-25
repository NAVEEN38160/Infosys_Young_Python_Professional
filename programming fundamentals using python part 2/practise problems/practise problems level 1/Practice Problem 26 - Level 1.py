def check_occurence(string):
    string=string.lower().split(" ")
    count_jet=0
    count_mat=0
    for word in string:
        if word=="jet":
            count_jet+=1
        if word=="mat":
            count_mat+=1
    if count_mat==count_jet:
        return True
    else:
        return False  

string = "Jet on the Mat but mat is too long"
print(check_occurence(string))