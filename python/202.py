class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stack = []
        while True:
            digit = list(str(n))
            total = 0
            for item in digit:
                total += int(item) ** 2
            if total == 1:
                return True
            if total in stack:
                return False
            stack.append(total)
            n = total


if __name__ == "__main__":
    a = Solution()
    print(a.isHappy(19))