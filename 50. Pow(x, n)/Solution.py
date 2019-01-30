class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == -1:
            return 1/x
        if n == 1:
            return x
        
        half = self.myPow(x, int(n/2))
        
        if n%2 == 0:
            return half*half
        else:
            if n > 0:
                return half*half*x
            else:
                return half*half*(1/x)