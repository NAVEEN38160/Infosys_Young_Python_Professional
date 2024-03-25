import math
def convert_to_roman(num):
    roman_num = {
        0:"",1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
        10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
        100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
        1000: "M", 2000: "MM", 3000: "MMM", 4000: "MMMM",
    }
    for key in roman_num.keys():
        if num==key:
            return roman_num[key]
    roman_reigns=""
    normal_number=str(num)
    for i in range(0,len(normal_number)):
        first_digit=int(int(normal_number)//math.pow(10,len(normal_number)-1))
        a=int(first_digit*math.pow(10,len(normal_number)-1))
        normal_number=str(int(normal_number)-a)
        roman_reigns+=roman_num[a]
    return roman_reigns

print(convert_to_roman(1043))