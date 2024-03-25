def validate_name(name):
    if len(name)==0:
        return False
    elif len(name)>15:
        return False
    elif not(name.isalpha()):
        return False
    else:
        return True

def validate_phone_no(phno):
    if len(phno)!=10:
        return False
    if not(phno.isdigit()):
        return False
    for i in range(0,len(phno)):
        count = 0
        for j in range(0,len(phno)):
            if phno[i]==phno[j]:
                count+=1
        if count==len(phno):
            return False
    return True

def validate_email_id(email_id):
    count_of_at=0
    for i in range(0,len(email_id)):
        if email_id[i]=="@":
            count_of_at+=1
    if count_of_at!=1:
        return False
    if not(email_id.endswith(".com")):
        return False
    domains = ["gmail","yahoo","hotmail"]
    at_index=email_id.index("@")
    com_index=email_id.index(".com")
    domain_name=email_id[at_index+1:com_index]
    if domain_name not in domains:
        return False
    return True

def validate_all(name,phone_no,email_id):
    count=0
    name_validation=validate_name(name)
    if not(name_validation):
        print("Invalid Name")
        count+=1
    phone_no_validation=validate_phone_no(phone_no)
    if not(phone_no_validation):
        print("Invalid phone number")
        count+=1
    email_id_validation=validate_email_id(email_id)
    if not(email_id_validation):
        print("Invalid email id")
        count+=1
    if count == 0:
        print("All the details are valid")
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9999999999", "tina@yahoo.com")