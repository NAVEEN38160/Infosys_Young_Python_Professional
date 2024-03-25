def check_well_formatted(input_item,list_label):
    if type(input_item) is not list:
        return False
    if len(input_item)<2:
        return False
    if input_item[0] not in list_label:
        return False
    count=0
    if type(input_item[0]) is int:
        count+=1
    for i in range(0,len(input_item)):
        if type(input_item[i])==str:
            count+=1
        if type(input_item[i])==list:
            a=check_well_formatted(input_item[i],list_label)
            if a:
                count+=1
    if count==len(input_item):
        return True
    else:
        return False

input_list1=[1,'3']
list_label1=[1,2]
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")