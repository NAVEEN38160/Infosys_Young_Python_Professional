def find_correct(word_dict):

    corr=0
    almost_corr=0
    wrong=0

    wrong_dict={}

    #start writing your code here
    for key,value in word_dict.items():
        if key == value :
            corr+=1
        elif key != value:
            wrong_dict.update({key:value})

    for key,value in wrong_dict.items():
        if len(key)==len(value):
            similar = 0
            notsimilar = 0
            for i in range(0,len(key)):
                if key[i]==value[i]:
                    similar+=1
                else:
                    notsimilar+=1
            if notsimilar>2:
                wrong+=1
            else:
                almost_corr+=1
        else:
            wrong+=1

    list=[corr,almost_corr,wrong]
    return list



word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))