def find_nine(nums):
    count=0
    for item in nums:
        if item==9:
            count+=1
    if count>0:
        if nums.index(9)<4:
            return True
        else:
            return False
    else:
        return False

nums = [1, 9, 4, 5, 6]
print(find_nine(nums))