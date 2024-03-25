def count_names(name_list):
    count1 = 0
    count2 = 0

    # start writing your code here
    # Populate the variables: count1 and count2

    for item in name_list:
        #if (len(item)==2 and item.startswith("at")):
           #count1 += 1
        if len(item)>2 and item.endswith("at"):
            count1 += 1
        if item.find("at")>=0:
            count2 += 1

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ",count1)
    print("%at% -> ",count2)


# Provide different names in the list and test your program
name_list1 = ["Hat", "Cat", "rabbit", "matter"]
name_list = ["at","dats"]
count_names(name_list)