
def count_evens(nums):
    result = 0
    for i in nums:
        if i % 2 == 0:
            result += 1
    return result
print(count_evens([1,2,3,5]))