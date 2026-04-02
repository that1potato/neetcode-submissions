class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        sell_price = buy_price
        idx = 1
        while idx < len(prices):
            if prices[idx] < buy_price:
                buy_price = prices[idx]
                sell_price = buy_price
            if prices[idx] > sell_price:
                sell_price = prices[idx]
                max_profit = sell_price - buy_price if sell_price - buy_price > max_profit else max_profit
            idx += 1
        return max_profit