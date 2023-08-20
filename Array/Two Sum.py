class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bucket = {} # initialize an empty dict
        for i, val in enumerate(nums): # iterate the nums with indx, val
            if val in bucket: 
                return [i, bucket[val]]
            bucket[target-val]=i # we use the complements as key and his indx as val                            
