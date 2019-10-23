import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return 2 ** int(math.log(n, 2)) == n


if __name__ == "__main__":
    a = Solution()
    print(a.isPowerOfTwo(6))