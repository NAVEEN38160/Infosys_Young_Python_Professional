def remove_duplicates(value):
    og_str=""
    for i in range(0,len(value)):
        if og_str.count(value[i])<1:
            og_str+=value[i]
    return og_str

print(remove_duplicates("222233435657uwqtqasda!"))