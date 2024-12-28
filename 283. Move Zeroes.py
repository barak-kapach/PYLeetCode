def move_zeroes_lose_data(nums):
    # the easy problem - we lose data during the sol
    ind = 0
    for n in nums:
        if n != 0:
            nums[ind] = n
            ind += 1
    return nums


print(move_zeroes_lose_data([0, 1, 0, 3, 12]))


def move_zeroes(nums):
    # we can use 2 ptrs
    l, r = 0, 0
    n = len(nums)
    while r < n:
        # if nums r is not 0
        if nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
        r += 1
    return nums

# check
print(move_zeroes([0, 1, 0, 3, 12]))
