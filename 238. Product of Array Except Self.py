def productExceptSelf(nums):
    """
    we initialize 2 arrays that represent the product from the left size and the right side

    """
    
    #we run on the pre -> the pre_prod[0] is 1 becuse 1 * x == x 
    # and we want to keep the product the same 
    # for the elements in the edgs
    pre_prod = [1] * (len(nums) + 1)
    for i in range(len(nums)):
        pre_prod[i + 1] = nums[i] * pre_prod[i]
    
    #as same as the pre prouduct we will do to the post pro
    post_prod = [1] * (len(nums) + 1)
    for i in range(len(nums) - 1, -1, -1):
        post_prod[i] = nums[i] * post_prod[i + 1]

    #now we have the product from right to left and left to right 
    res = [0] * len(nums)
    for i in range(len(res)):
        res[i] = pre_prod[i] * post_prod[i + 1]
    
    return res

productExceptSelf([1,2,3,4])