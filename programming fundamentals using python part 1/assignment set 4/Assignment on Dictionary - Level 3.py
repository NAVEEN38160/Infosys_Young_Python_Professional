def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    P = 0
    O = 0
    E = 0
    for i in range(0,len(patient_medical_speciality_list)):
        if i%2!=0:
            if patient_medical_speciality_list[i] == "P":
                P+=1
            elif patient_medical_speciality_list[i]=="O":
                O+=1
            elif patient_medical_speciality_list[i]=="E":
                E+=1
    
    speciality=("")
    list=[P,O,E]
    max=""
    if list[0]>list[1]:
        if list[0]>list[2]:
            max+="P"
        else:
            max+="E"
    elif list[1]>list[2]:
        if list[1]>list[0]:
            max+="O"
        else:
            max+="P"
    else :
        max+="E"
        
    for key,value in medical_speciality.items():
        if key == max:
            speciality+=value
            
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)