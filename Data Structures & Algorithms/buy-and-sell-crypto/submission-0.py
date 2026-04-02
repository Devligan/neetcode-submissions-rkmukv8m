class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxMoney = 0
        currCheapest = prices[0]
        for i in range(1, len(prices)):
            maxMoney = max(maxMoney, prices[i] - currCheapest)
            currCheapest = min(currCheapest, prices[i])
        return maxMoney