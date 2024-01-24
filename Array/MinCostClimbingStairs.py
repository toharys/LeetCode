class Solution(object):

    # non efficient solution O(2^n): recursive tree in height of n which splits to 2 in each stage
    # def minCostClimbingStairs(self, cost):
    #     """
    #     :type cost: List[int]
    #     :rtype: int
    #     """
    #     def _helper(curr):
    #         if curr<=1:
    #             return cost[curr]
    #         return cost[curr] + min(
    #             _helper(curr-1),
    #             _helper(curr-2)
    #         )
        
    #     return min(_helper(len(cost)-1), _helper(len(cost)-2))