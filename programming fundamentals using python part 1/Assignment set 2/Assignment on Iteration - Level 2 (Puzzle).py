def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    if legs % 2 != 0 or heads == 0 or heads > legs:
        print(error_msg)
    else:
        r = int((legs + (-2 * heads)) / 2)
        c = int(heads - r)
        chicken_count=c
        rabbit_count=r
        print(chicken_count, rabbit_count)
        #Populate the variables: chicken_count and rabbit_count
        


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(150,400)