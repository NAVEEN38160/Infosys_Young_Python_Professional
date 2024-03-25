def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    if len(data1)==len(data2) and set(data1)==set(data2):
        count=0
        for i in range(0,len(data1)):
            if data1[i] in data2 and data1[i]!=data2[i]:
                count+=1
        if count == len(data1):
            return True
        else:
            return False
    else:
        return False

print(check_anagram("resell","scller"))