def has22(nums): 
    indices = []
    for i in range(0, len(nums)):
        if nums[i] == 2: 
            indices.append(i)
    for i in range(0, len(indices)-1):
        if indices[i+1] - indices[i] == 1:
            return True
    return False
