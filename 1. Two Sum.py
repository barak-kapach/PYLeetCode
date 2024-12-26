def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = dict()
    
    for i in range(len(nums)):
        if nums[i] in d:
            return d[nums[i]], i
        else:
            d[target- nums[i]] = i

print(twoSum([2,7,11,15], 9))