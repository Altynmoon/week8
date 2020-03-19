def sum67(nums): 
    dontadd = 0
    sum = 0
    for i in range(0, len(nums)):
        if dontadd == 0:
            if nums[i] == 6: 
                dontadd = 1
            else:
                sum += nums[i]
        else:
            if nums[i] == 7: 
                dontadd = 0
            else:
                pass 
    return sum
