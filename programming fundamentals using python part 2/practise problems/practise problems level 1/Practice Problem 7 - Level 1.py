def seed_no(number, ref_no):
    str_no=str(number)
    list1=list(str_no)
    for item in list1:
        number*=int(item)
    if number==ref_no:
        return True
    else:
        return False

number = 123
ref_no = 738
print(seed_no(number, ref_no))