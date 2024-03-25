#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum=0
    for item in list_of_marks:
        sum+=item
    avg=sum/len(list_of_marks)
    count=0
    for item in list_of_marks:
        if item>avg:
            count+=1
    return (count/len(list_of_marks))*100

def sort_marks():
    sort=sorted(list_of_marks)
    return sort

def generate_frequency():
    frq=[]
    for i in range(0,26):
        if i in list_of_marks:
            count=list_of_marks.count(i)
            frq.append(count)
        else:
            frq.append(0)
    return frq

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())