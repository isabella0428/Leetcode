import math


class Solution1:
    def myPow(self, x, n):          #math method
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        sign = -1 if x < 0 and n % 2 == 1 else 1
        x = abs(x)
        log_term = n * math.log(x, 2)
        result = 2 ** log_term
        return sign * result


class Solution2:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        return self.myPow(x * x, int(n / 2)) if n % 2 == 0 else x * self.myPow(x * x, int(n / 2))


if __name__ == "__main__":
    a = Solution2()
    print(a.myPow(2.1, 4))


