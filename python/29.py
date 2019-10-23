import math
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not dividend:
            return 0
        sign = 1 if dividend * divisor > 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0

        log_ans = math.log(dividend, 2) - math.log(divisor, 2)
        ans = sign * int(2 ** log_ans + 1) if 2 ** log_ans - int(2 ** log_ans) > 0.9999 \
            else sign * int(2**log_ans)
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 2 ** 31 - 1
        else:
            return ans


if __name__ == "__main__":
    a = Solution()
    print(a.divide(-2147483648,
2))