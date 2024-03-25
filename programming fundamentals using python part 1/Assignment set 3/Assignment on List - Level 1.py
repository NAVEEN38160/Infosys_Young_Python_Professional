def find_leap_years(given_year):
    list_of_leap_years=[]

    closest_leap_year=0

    if given_year%4==0:
        closest_leap_year = given_year
    elif given_year % 4 == 1:
        closest_leap_year = given_year + 3
    elif given_year % 4 == 2:
        closest_leap_year = given_year + 2
    elif given_year % 4 == 3:
        closest_leap_year = given_year + 1
    else:
        print("enter a valid year")

    #Write your logic here
    for i in range(0,15):
        if closest_leap_year%100==0 and closest_leap_year%400!=0:
            closest_leap_year+=4
        list_of_leap_years.append(closest_leap_year)
        closest_leap_year+=4

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)

