def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    invalid=-1
    vp=120
    nvp=150
    tc=0
    fc=0

    #write your logic here

    if quantity_ordered >=1 and distance_in_kms>0 and (food_type == 'N' or food_type=='V'):
        if distance_in_kms <= 3:
            tc = 0
        elif distance_in_kms <= 6:
            tc = (distance_in_kms - 3) * 3
        else:
            tc = ((distance_in_kms - 6) * 6) + 9

        if food_type == "N":
            fc = nvp * quantity_ordered
        elif food_type == "V":
            fc= vp * quantity_ordered
        else:
            return invalid

        bill_amount = tc+fc
        return bill_amount
    else:
        return invalid

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,1)
print(bill_amount)