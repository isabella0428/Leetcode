class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        first_buy, second_buy = float('-inf'), float('-inf')
        first_sell, second_sell = 0, 0
        for price in prices:
            first_buy = -price if first_buy < -price else first_buy
            first_sell = first_buy + price if first_sell < first_buy + price else first_sell
            second_buy = first_sell - price if second_buy < first_sell - price else second_buy
            second_sell = second_buy + price if second_sell < second_buy + price else second_sell
        return max(first_sell, second_sell)


if __name__ == "__main__":
    a = Solution()
    print(a.maxProfit([3,3,5,0,0,3,1,4]))