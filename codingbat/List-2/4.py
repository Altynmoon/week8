def sum13(nums): 
    sum = 0
    for i in range(0, nums.count(13)):
        if nums.count(13):
            after = nums.index(13)
            nums.remove(13)
            if after < len(nums): 
                    nums.pop(after)
    for i in nums: 
        sum += i
    return sum
