def calculate(distance,no_of_passengers):
    total_tkt_coll=no_of_passengers*80
    fuel_price=(distance/10)*70
    margin=total_tkt_coll-fuel_price
    if margin>0:
        return margin
    else:
        return -1

distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))