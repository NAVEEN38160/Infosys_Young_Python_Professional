def calculate_net_amount(trans_list):
    total_deposit=0
    total_withdrawal=0
    for item in trans_list:
        split_items=item.split(":")
        if split_items[0]=="D":
            total_deposit+=int(split_items[1])
        else:
            total_withdrawal+=int(split_items[1])
    net_amount=total_deposit-total_withdrawal
    return net_amount

trans_list = ["D:300", "D:200", "W:200", "D:100"]
print(calculate_net_amount(trans_list))