def human_pyramid(no_of_people):
    #place the recursive code the you had written earlier for this function
    if no_of_people==1:
        return no_of_people*50
    else:
        return (no_of_people*50)+(human_pyramid(no_of_people-2))

def find_maximum_people(max_weight):
    no_of_people=0
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable
    max_person=max_weight//50
    if max_person%2==0:
        max_person-=1
    for i in range(1,max_person+1,2):
        result=human_pyramid(i)
        if result<=max_weight:
            no_of_people=i
    return no_of_people

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)



