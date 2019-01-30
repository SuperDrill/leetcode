class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        m = [0 for x in range(amount+1)]
        m[0] = 1
        for coin in coins:
            for num in range(amount+1):
                if num - coin >= 0:
                    m[num] += m[num-coin]
        return m[amount]