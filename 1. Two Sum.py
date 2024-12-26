def twoSum(nums, target):
    """
    run time is O(n) because we run on the array once
    and the space is O(n) 0-> we use a dict to store the values

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

def two_sum_with_2ptrs(nums, target):
    """
    run time is O(nlogn) because we sort the array
    and the space is O(1) 0-> we dont use any extra space just 2 ptrs

    :param nums:
    :param target:
    :return:
    """
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return l, r
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    #if we didnt find any sol
    return -1, -1
print(twoSum([2,7,11,15], 9))