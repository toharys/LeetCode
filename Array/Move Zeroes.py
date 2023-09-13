class Solution(object):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    def moveZeroes(self, nums):
        lastZero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastZero], nums[i] = nums[i],nums[lastZero]
                lastZero+=1                   
