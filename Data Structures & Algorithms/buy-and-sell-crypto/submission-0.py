class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minl=prices[0]
        curr=0
        profit=0
        for i in range(1,len(prices)):
            curr=prices[i]-minl
            profit=max(profit,curr)
            minl=min(minl,prices[i])
        return profit