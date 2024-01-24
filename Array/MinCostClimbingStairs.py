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


# an efficient solution O(n): based on DP approach, table 1Xn each cell computable in O(1)
    def minCostClimbingStairs(self, cost):
    #     """
    #     :type cost: List[int]
    #     :rtype: int
    #     """
        dp = [0]*len(cost)
        n = len(cost)-1
        dp[0] = cost[n]
        dp[1] = cost[n-1]

        for i in range(2,len(cost)):
            dp[i] = cost[n-i] + min( dp[i-1] , dp[i-2])

        return min( dp[-1], dp[-2]) 