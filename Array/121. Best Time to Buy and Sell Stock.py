# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
# Approach1
    def maxProfit(self, prices):
        buying_price = prices[0]
        profit = 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]<buying_price:
                buying_price = prices[i]
            else:
                profit = prices[i] - buying_price
                if profit>max_profit:
                    max_profit = profit
        return max_profit

# Approach2
        # for i in range(len(prices)-1):
        #     if prices[i]>=prices[i+1]:
        #         continue
        #     if prices[i]>=buy:
        #         continue
        #     buy=prices[i]
        #     for j in range(i+1,len(prices)):
        #         if (prices[j]-prices[i])>profit:
        #             profit = prices[j]-prices[i]
        #     i = i + 1
        # return profit