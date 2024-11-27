from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices [r]:
                profit = prices [r] - prices [l]
                if (profit > maxProfit):
                    maxProfit = profit
            else:
                l = r
            r += 1

        return maxProfit 
    

solucao = Solution()
print(solucao.maxProfit ([1,2,3]))