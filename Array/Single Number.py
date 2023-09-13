class Solution(object):
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res = res^num # bitwise logical xor
        return res
