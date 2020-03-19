def array_front9(nums):
    result = False
    for i in range(4):
        if len(nums) > i:
            if nums[i] == 9:
                result = True
    return result
print(array_front9([1,2,,2,4]))