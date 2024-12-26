"""
neet code solution for the problem
"""
def minSubArrayLen(target, nums):
    best_counter = len(nums) + 1
    cur_sum = 0
    l = 0
    
    for r in range(len(nums)):
        cur_sum += nums[r]
        while cur_sum >= target:
            best_counter = min(best_counter, r - l + 1)
            cur_sum -= nums[l]
            l += 1
    return 0 if best_counter == len(nums) + 1 else best_counter


#tests 
t = 7
nums = [2,3,1,2,4,3]
nums2 = [1,4,4]
print(minSubArrayLen(5, nums2))