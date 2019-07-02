# Say you have an array for which the ith element is the price
# of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e.,
#  buy one and sell one share of the stock), design an algorithm to find
#  the maximum profit.


# MAx profit using dym=namic programming 

def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        
        l = len(prices)
        
        dp = [0]*l
        
        for i in range(1,l):
             dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], 0) 
        
        return max(dp)
    

