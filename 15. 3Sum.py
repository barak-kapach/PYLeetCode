def threeSumNaiveSol(nums):
    """
    run time -> 
    the first 3 loops -> O(n**3)
                        in the third loop we check if valid [i,j,k] is 
                        in res.. in the worst case we get that this is will be O(n) alse
                        than the total time is O(n**4)
    """
    res = []
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])

    return res

def threeSumWithHashMap(nums):
    """
    in this sol we seperate the problem 
    at first we sort the array, and than, we run on every index i 
        - now we solve 2 sum problem with the the input -> nums[i] and the subarray nums[i:len(nums)]
    """
    nums.sort()
    last_val = None
    result = []
    for i in range(len(nums)): # we can do that from 1 to n-2
        #solve 2sum on the sub array nuns[i:len(nums)] and the value of nums i
        if nums[i] != last_val:
            #we can solve 2sum
            last_val = nums[i]
            target = (nums[i])*(-1) # target + b + c = 0 -> we want b + c = -target
            d = dict()
            section = []
            for j in range(i+1, len(nums)):
                if nums[j] in d:
                    check_triple = [target*(-1), nums[j], d[nums[j]]]
                    check_triple.sort()
                    if check_triple not in section:
                        result.append(check_triple)
                        section.append(check_triple)
                else:
                    d[target - nums[j]] = nums[j]
    return result


def threeSumWithleftAndRightPtr(nums):
    result = []
    nums.sort()
    for i, val in enumerate(nums):
        if i > 0 and val == nums[i - 1]:
            continue
        #solve 2sum with 2 ptrs
        l, r = i + 1 , len(nums) - 1
        while l < r:
            triple_sum = val + nums[l] + nums[r]
            if triple_sum > 0:
                r -= 1
            elif triple_sum < 0:
                l -= 1
            else:
                result.append([val, nums[l], nums[r]])
                # in this secion we want to update our ptrs but in the correct way
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1 

    return result




nums = [-1,0,1,2,-1,-4]
print(threeSumNaiveSol(nums))
print(threeSumWithHashMap(nums))