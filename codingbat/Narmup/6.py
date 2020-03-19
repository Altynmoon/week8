def array_count9(nums):
    result = 0
    for i in nums:
        if i == 9:
            result += 1
    return result
print(array_count9([1,2,9]))
