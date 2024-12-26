def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    #the array is sorted
    #we can use 2 ptrs.
    #if the sum of  numbers[l] + numbers[r] ><== target we can increase decrease or return 
    while l < r:
        val = numbers[l] + numbers[r]
        print(l, r, val)
        #sum < target 
        if val < target:
            l += 1
        #sum > target
        elif val > target:
            r -= 1
        
        #sum == target 
        elif val == target:
            return [l + 1, r + 1]
        
print(twoSum( [2,3,4],6))