# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.



def maxProfit(prices):
        # Brute force 
        max_profit = 0 
        min_price = 9223372036854775807
        
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
                
            else:
                max_profit = max(max_profit,prices[i]-min_price)
                
        return max_profit
    
    
