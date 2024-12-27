from operator import truediv
from xmlrpc.client import MAXINT

from scipy.stats import false_discovery_control


def increasingTripletNaiveSol(nums):
    """
    this sol is naive because we run on the array 3 times
    and the run time is O(n**3)
    :param nums: list[int]
    :return: true if there is a triplet else false
    """
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] < nums[j] and nums[j] < nums[k]:
                    return True
    return False
# #check
# print(increasingTripletNaiveSol([1,2,3,4,5])) #True
# print(increasingTripletNaiveSol([5,4,3,2,1])) #False
# print(increasingTripletNaiveSol([2,1,5,0,4,6])) #True

def increasingTriplet(nums):
    """
    we can solve this problem with O(n) run time and O(1) space
    assumption: we can say that triplet in subarray is also triplet in the arr
    we can iterate the arr and save the local min.
    after we have a local min we can solve the problem to a length 2 seq
    :param nums:
    :return:
    """
    # we can say that triplet in subarray is also triplet in the arr
    # we can iterate the arr and save the local min.
    #after we have a local min we can solve the problem to a length 2 seq
    #we know that the condition to the seq is grater than
    a1 = MAXINT
    a2 = MAXINT
    for n in nums:
        if n <= a1:
            #we can use n as a local min in the subarray
            a1 = n
        elif n <= a2:
            # we know that  -> n > a1
            a2 = n
        else:
            #we know that -> n > a2 > a1
            #we have a triplet ->  a1 < a2 < n(cur_n)
            return True
    return False

#check
aaa =[2,4,-2,-3]
# print(increasingTriplet([1,2,3,4,5])) #True
print(increasingTriplet(aaa))